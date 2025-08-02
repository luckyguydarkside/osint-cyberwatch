import requests
from urllib.parse import urlparse

# Function to fetch and analyze HTTP headers of a given URL
def analyze_http_headers(url):
    """Fetches HTTP headers from the specified URL and returns a summary."""
    try:
        # Send a HEAD request to the URL to fetch headers
        response = requests.head(url, allow_redirects=True)
        
        # Extract relevant header information
        headers = response.headers
        
        # Create a summary dictionary
        summary = {
            'URL': url,
            'Status Code': response.status_code,
            'Content-Type': headers.get('Content-Type'),
            'Server': headers.get('Server'),
            'Content-Length': headers.get('Content-Length'),
            'X-Frame-Options': headers.get('X-Frame-Options'),
            'Strict-Transport-Security': headers.get('Strict-Transport-Security'),
        }
        
        return summary
    
    except requests.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return None

def main():
    # Input: URL to analyze
    target_url = input("Enter a URL to analyze (e.g., https://example.com): ")
    
    # Parse the URL to validate it
    parsed_url = urlparse(target_url)
    if not parsed_url.scheme:
        target_url = 'http://' + target_url  # Default to HTTP if no scheme is provided
    
    # Analyze the HTTP headers
    header_summary = analyze_http_headers(target_url)
    
    # Output the results
    if header_summary:
        print("\nHTTP Headers Summary:")
        for key, value in header_summary.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```