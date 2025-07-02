import os
import string
import random
import hashlib
from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)

# Connect to Redis
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = os.environ.get('REDIS_PORT', 6379)
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# Length of the shortened URL code
SHORT_CODE_LENGTH = 6

def generate_short_code(url):
    """Generate a short code for a URL using a combination of hashing and randomization"""
    # Create a hash of the URL to ensure some uniqueness
    hash_object = hashlib.md5(url.encode())
    hash_digest = hash_object.hexdigest()
    
    # Use the hash as a seed for randomization
    random.seed(hash_digest)
    
    # Generate a short code using letters and numbers
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(SHORT_CODE_LENGTH))
    
    return short_code

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """API endpoint to shorten a URL"""
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    original_url = data['url']
    
    # Check if this URL has already been shortened
    existing_code = redis_client.get(f"url:{original_url}")
    if existing_code:
        short_code = existing_code
    else:
        # Generate a new short code
        short_code = generate_short_code(original_url)
        
        # Check if this code already exists (collision handling)
        while redis_client.exists(f"code:{short_code}"):
            short_code = generate_short_code(original_url + str(random.random()))
        
        # Store the mappings in both directions
        redis_client.set(f"code:{short_code}", original_url)
        redis_client.set(f"url:{original_url}", short_code)
    
    # Get the host from the request, or use a default
    host = request.headers.get('Host', request.host)
    shortened_url = f"http://{host}/{short_code}"
    
    return jsonify({
        'original_url': original_url,
        'shortened_url': shortened_url,
        'short_code': short_code
    })

@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    """Redirect from a short code to the original URL"""
    original_url = redis_client.get(f"code:{short_code}")
    
    if original_url:
        return redirect(original_url)
    else:
        return jsonify({'error': 'URL not found'}), 404

@app.route('/', methods=['GET'])
def home():
    """Simple home page"""
    return jsonify({
        'message': 'URL Shortener API',
        'endpoints': {
            '/shorten': 'POST - Shorten a URL',
            '/<short_code>': 'GET - Redirect to original URL'
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
