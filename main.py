import sys
from crawl import crawl_page


def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    
    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = sys.argv[1]

    print(f"starting crawl of: {base_url}...")

    try:
        page_data = crawl_page(base_url)
    except Exception as e:
        print(f"Error fetching HTML from {base_url}: {str(e)}")
        sys.exit(1)

    print(f"Found {len(page_data)} pages:")
    for page in page_data.values():
        print(f"- {page['url']}: {len(page['outgoing_links'])} outgoing links")

    sys.exit(0)


if __name__ == "__main__":
    main()
