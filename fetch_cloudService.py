import requests
import pandas as pd

# Base URLs and credentials
hotel_base_url = "https://hotel-author.adobeprod.microsoft.com/content/campaigns/{brand}/en-us.1.json"
hotel_username = "integration_campaign_remote"
hotel_password = "PssWswh5v_9HRY-"

monolith_base_url = "https://sites-author.adobeprod.microsoft.com/content/campaigns/{brand}/en-us.1.json"
monolith_username = "integration_campaign_remote"
monolith_password = "J-X/s$0ZzQ2(7&f"

# List of brands to iterate
# List of brands to iterate
brands = [
    "edge-consumer", "microsoft-365-consumer", "msa-consumer", "rewards-consumer", "surface-consumer",
    "windows-consumer", "gmo-cloud-skills", "designer", "microsoft-edu", "azure", "dynamics-365-commercial",
    "industry-commercial", "isv", "microsoft-365-commercial", "microsoft-security", "ms-learn",
    "power-platform-commercial", "teams", "visual-studio", "windows-365-commercial", "copilot-studio", "github",
    "m365-partner-readiness", "microsoft-365-developer-program", "microsoft-advertising", "microsoft-unified", "oem",
    "microsoft-store-email", "survey-cpe", "survey-ri", "tfl", "gmo-vss-dev-audiences", "windows-insider-program",
    "one-drive-consumer", "field-marketing", "discover-try-buy", "wwl-gtm", "azure-cosmos", "azure-marketplace",
    "azure-speech", "bap-success", "cloud-experience-studio-cxs", "cpm-notifications", "csp-insider",
    "customer-connection", "defender-experts", "dev-compute", "devdiv-ux", "fabric", "gdx-analytics",
    "global-content-studio", "gmo-m365-developer", "growth-ecosystems", "grs", "imagine-cup",
    "m365-fasttrack-engineering", "microsoft-365-lighthouse", "platform-content", "powerplatforms", "ux-research",
    "xbox"
]

# List to store results
results = []

# Iterate over each brand
for brand in brands:
    # Construct URLs for both servers
    hotel_url = hotel_base_url.format(brand=brand)
    monolith_url = monolith_base_url.format(brand=brand)

    # Fetch data from Hotel server
    hotel_response = requests.get(hotel_url, auth=(hotel_username, hotel_password))
    hotel_cq_cloudserviceconfigs = None
    if hotel_response.status_code == 200:
        hotel_data = hotel_response.json()
        hotel_cq_cloudserviceconfigs = hotel_data.get("jcr:content", {}).get("cq:cloudserviceconfigs", None)
    else:
        hotel_cq_cloudserviceconfigs = f"Error {hotel_response.status_code}"

    # Fetch data from Monolith server
    monolith_response = requests.get(monolith_url, auth=(monolith_username, monolith_password))
    monolith_cq_cloudserviceconfigs = None
    if monolith_response.status_code == 200:
        monolith_data = monolith_response.json()
        monolith_cq_cloudserviceconfigs = monolith_data.get("jcr:content", {}).get("cq:cloudserviceconfigs", None)
    else:
        monolith_cq_cloudserviceconfigs = f"Error {monolith_response.status_code}"

    # Append the result to the list
    results.append({
        "Brand": brand,
        "Hotel URL": hotel_url,
        "Hotel cq:cloudserviceconfigs": hotel_cq_cloudserviceconfigs,
        "Monolith URL": monolith_url,
        "Monolith cq:cloudserviceconfigs": monolith_cq_cloudserviceconfigs
    })

# Create a DataFrame from the results
df = pd.DataFrame(results)

# Save the DataFrame to an Excel file
df.to_excel("output.xlsx", index=False)

print("Results have been exported to 'output.xlsx'")