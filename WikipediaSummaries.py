import requests  # Importing the requests module to make HTTP requests
import json  # Importing the json module to handle JSON data

def get_wikipedia_summary(topic):
    # Constructing the URL to fetch Wikipedia summary based on the given topic
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    try:
        # Making a GET request to fetch data from the URL
        response = requests.get(url)
        # Checking if the response status code is 200 (indicating success)
        if response.status_code == 200:
            # Extracting JSON data from the response
            data = response.json()
            # Extracting the summary text from the JSON data
            summary = data["extract"]
            # Extracting the URL of the thumbnail image (if available) from the JSON data
            image_url = data.get("thumbnail", {}).get("source")
            # Returning the summary text and the image URL
            return summary, image_url
        else:
            # Returning an error message if fetching information failed
            return "Failed to fetch information. Please try again later.", None
    except requests.RequestException as e:
        # Returning an error message if an exception occurred during the request
        return f"An error occurred: {e}", None

def save_image_from_url(image_url, filename):
    try:
        # Making a GET request to fetch the image data from the given URL
        response = requests.get(image_url)
        # Checking if the response status code is 200 (indicating success)
        if response.status_code == 200:
            # Opening a file in binary write mode to save the image data
            with open(filename, "wb") as f:
                # Writing the image data to the file
                f.write(response.content)
            print(f"Image saved successfully as {filename}")
        else:
            print("Failed to fetch image!")
    except requests.RequestException as e:
        # Printing an error message if an exception occurred during the request
        print(f"An error occurred while fetching the image: {e}")

def main():
    print("Welcome to Wikipedia summaries!")
    topic = input("Enter a topic you want to learn more about: ")
    # Calling the get_wikipedia_summary function to fetch the summary and image URL
    summary, image_url = get_wikipedia_summary(topic)
    # Printing the summary text
    print("\nSummary:")
    print(summary)
    
    # Checking if an image URL is available
    if image_url:
        # Generating a filename for the image based on the topic
        filename = f"{topic.replace(' ', '_')}.jpg"  # Example filename
        # Calling the save_image_from_url function to save the image
        save_image_from_url(image_url, filename)
    else:
        # Printing a message if no image is available for the topic
        print("\nNo image available for this topic.")

if __name__ == "__main__":
    main()
