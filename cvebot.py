import requests
import openai

# Configuration
base_url = "https://services.nvd.nist.gov"
api_endpoint = "/rest/json/cves/1.0"
output_file = "vulnerabilities.txt"  # Specify the output file name

openai.api_key = "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"

chathistory = [
    {"role": "system", "content": "You are a Discord Bot that is powered by OpenAI. You are an absolute CHAD. Your name is ChadGPT."},
]

def fetch_latest_vulnerabilities():
    # Send request to NVD API
    url = base_url + api_endpoint
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        if "result" in data:
            # Extract the latest vulnerabilities
            vulnerabilities = data["result"]["CVE_Items"]

            with open(output_file, "w") as file:
                for vuln in vulnerabilities:
                    # Extract relevant information
                    cve_id = vuln["cve"]["CVE_data_meta"]["ID"]
                    description = vuln["cve"]["description"]["description_data"][0]["value"]
                    published_date = vuln["publishedDate"]

                    # Write the vulnerability details to the file
                    file.write(f"CVE ID: {cve_id}\n")
                    file.write(f"Description: {description}\n")
                    file.write(f"Published Date: {published_date}\n")
                    file.write("----------------------\n")

            print("Vulnerabilities written to vulnerabilities.txt.")

            # Read the contents of the vulnerabilities file
            with open("vulnerabilities.txt", "r") as file:
                file_contents = file.read()

                # Append the file contents to the chat history
                chathistory.append({"role": "system", "content": "Here is a list of new vulnerabilities. Compare this list with a list that will follw this one of known assets for the company. If one of the vulnerabilities relates to a known asset, reply with the specific information about that vulnerability."})
                chathistory.append({"role": "system", "content": file_contents})

            # Read the contents known assets file
            with open("knownassets.txt", "r") as file:
                file_contents = file.read()

                # Append the file contents to the chat history
                chathistory.append({"role": "system", "content": "Here is the list of known assets. Look at this list and if any of the vulnerabilites above relate to any of these, reply with the specific information about that vulnerability."})
                chathistory.append({"role": "system", "content": file_contents})


            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=chathistory,
                temperature=0.3,
            )
            reply = response.choices[0].message.content
            chathistory.append({"role": "assistant", "content": reply})
            print(reply)

        else:
            print("No vulnerabilities found.")

    else:
        print("Failed to retrieve data from the NVD API.")


# Fetch the latest vulnerabilities
fetch_latest_vulnerabilities()
