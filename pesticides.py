def get_pesticide_recommendations(disease_class):
    recommendations = {
        "Stem and Rot Mango":[
            "1.Use Disease-Resistant Varieties: Plant resistant mango cultivars to minimize the incidence of stem rot. These varieties are specifically bred to withstand various diseases, ensuring better yield and health.",
            "2.Proper Water Management: Avoid overwatering and ensure proper drainage to prevent waterlogging. Excess moisture creates an environment conducive to fungal growth, leading to stem rot.",
            "3.Sanitation Practices: Regularly inspect trees and promptly remove any infected branches or stems. Proper disposal of infected materials is crucial to prevent the spread of the disease in the orchard.",
            "4.Soil Health Management: Imp  rove soil structure by adding organic matter, like compost, to enhance drainage. Healthy soil promotes strong root development, reducing the likelihood of root and stem diseases.",
            "5.Fungicide Application: Apply appropriate fungicides preventively, especially during wet conditions or at the first sign of symptoms. Following recommended rates and guidelines ensures effective control of the disease."
        ],

        "Black Mould Rot mango": [
            "1. Fungicide Application: Apply fungicides like Mancozeb or Copper Oxychloride during flowering and fruit development. Follow label instructions for proper rates and timing.",
            "2. Sanitation Practices: Regularly remove infected fruits, leaves, and debris from the orchard. This reduces pathogen spread and minimizes the inoculum in the environment.",
            "3. Proper Irrigation Management: Avoid overwatering to prevent waterlogging, which promotes fungal growth. Use drip irrigation to maintain soil moisture without wetting foliage.",
            "4. Post-Harvest Handling: Minimize mechanical injury during harvesting to prevent wounds that facilitate infection. Store harvested fruits in a cool, dry place to reduce mold growth.",
            "5. Crop Rotation and Diversification: Rotate crops with non-host plants to break the disease cycle. This helps reduce soil-borne pathogens and lowers the risk of infection."
        ],
        
        "Alternaria mango": [
            "1.Fungicide Application: Use fungicides like Chlorothalonil, Mefenoxam, or Azoxystrobin during flowering and fruit development, following label instructions for dosage and timing.",
            "2.Sanitation Practices: Regularly remove and dispose of infected leaves, fruits, and debris to reduce disease spread.",
            "3.Water Management: Implement drip irrigation to minimize leaf wetness and humidity, limiting infection rates.",
            "4.Nutrient Management: Provide balanced nutrition, especially potassium, while avoiding excessive nitrogen to enhance disease resistance.",
            "5.Monitoring: Keep an eye on weather conditions and monitor for early signs of infection, timing fungicide applications before high disease pressure periods."
        ],
        
        "Anthracnose mango": [
            "1. Fungicide Application: Use systemic fungicides like Thiophanate-methyl or Mancozeb at flowering onset and during fruit development. Follow label instructions for best results.",
            "2. Cultural Practices: Regularly remove fallen and infected fruits and debris to limit the spread of infection.",
            "3. Water Management: Avoid overhead irrigation, which increases humidity. Use drip irrigation to keep leaves dry.",
            "4. Nutrient Management: Provide balanced nutrition, focusing on potassium for disease resistance. Avoid excess nitrogen.",
            "5. Timing of Applications: Monitor for early signs of Anthracnose, especially in wet conditions. Apply fungicides preventively."
        ],

        
        "Black Spot Papaya": [
            "1. Use Resistant Varieties: Plant Resistant Cultivars: Choose papaya varieties that are resistant to Papaya ringspot virus (PRSV), such as 'Red Lady' or 'Sunset,' to minimize disease susceptibility.",
            "2. Control Aphids: Aphid Management: Use insecticides or introduce natural predators to reduce aphid populations, as they are primary vectors for the virus.",
            "3. Sanitation Practices: Remove Infected Plants: Regularly inspect and remove any infected papaya plants immediately to prevent the virus from spreading.",
            "4. Crop Rotation: Rotate Crops: Avoid planting papayas in the same location year after year and rotate with non-host crops to break the virus's life cycle.",
            "5. Physical Barriers: Use Row Covers: Protect young plants with floating row covers or mesh to prevent aphids and other insect vectors from reaching them."
        ],
        
        "blackspot orange": [
            "1. Use Resistant Varieties: Select Resistant Cultivars: Choose orange varieties that are resistant or tolerant to black spot disease to minimize the risk of infection.",
            "2. Fungicide Application: Apply Fungicides: Use appropriate fungicides during the flowering and fruit development stages to protect against infection. Follow label instructions for application rates and timing.",
            "3. Proper Pruning and Spacing: Enhance Airflow: Prune trees to improve airflow and reduce humidity around the foliage, creating less favorable conditions for fungal growth. Proper spacing between trees can also help.",
            "4. Sanitation Practices: Remove Infected Material: Regularly inspect trees and remove any infected leaves or fruit to prevent the spread of the disease. Dispose of debris away from the orchard.",
            "5. Monitor Environmental Conditions: Track Weather Conditions: Be aware of wet and humid conditions, which promote fungal growth. Monitor for disease signs and take preventive actions during favorable conditions."
        ],
        
        "grenning orange": [
            "1. Select Resistant Cultivars: Choose orange varieties that have been bred for tolerance to greening disease, such as 'Valencia' or 'Pineapple' oranges.",
            "2. Manage Aphids and Psyllids: Use targeted insecticides to control Asian citrus psyllids, the primary vectors of the greening bacterium.",
            "3. Provide Proper Nutrition: Maintain a balanced fertilization program to ensure trees are healthy and more resistant to diseases.",
            "4. Inspect Trees Regularly: Conduct regular inspections of your orchards for symptoms of greening disease.",
            "5. Implement Good Cultural Practices: Practice proper irrigation management to avoid overwatering."
        ],
        
        "Healthy Guava": [
            "1. Maintain good practices, no pesticides needed."
        ],
        
        "Healthy mango": [
            "1. Keep the tree healthy, no pesticides needed."
        ],
        
        "Healthy Orange": [
            "1. Monitor for pests; no immediate action needed."
        ],
        
        "Healthy Papaya": [
            "1. Keep healthy practices, no pesticides needed."
        ],
        
        "Phytopthora Guava": [
            "1. Use Resistant Varieties: Choose guava varieties that are resistant or tolerant to Phytophthora, such as 'Allahabad Safeda' or 'Barakhan'.",
            "2. Fungicide Application: Use systemic fungicides like Ridomil Gold (metalaxyl) or Phosphonate products for effective control.",
            "3. Soil Management: Improve Soil Drainage: Ensure proper drainage in planting areas to prevent waterlogging.",
            "4. Sanitation Practices: Remove Infected Material: Regularly inspect guava plants for signs of infection and remove any infected plants or debris promptly.",
            "5. Irrigation Practices: Avoid Overhead Irrigation: Use drip irrigation instead of overhead sprinklers to minimize moisture on the foliage."
        ],
        
        "Powdery Mildery Papaya": [
            "1. Apply Fungicides: Use systemic fungicides such as Triadimefon, Propiconazole, or Myclobutanil to control powdery mildew.",
            "2. Preventive Treatments: Use Sulfur-Based Fungicides: Apply sulfur-based fungicides as a preventive measure.",
            "3. Cultural Practices: Improve Airflow: Prune papaya plants to enhance airflow around the foliage.",
            "4. Sanitation Practices: Remove Infected Plant Material: Regularly inspect papaya plants and remove any infected leaves or fruits.",
            "5. Water Management: Avoid Overhead Irrigation: Implement drip irrigation instead of overhead sprinklers."
        ],
        
        "Ring spot Papaya": [
            "1. Use Resistant Varieties: Plant resistant papaya varieties, such as 'Red Lady' or 'Sunset', to minimize susceptibility to Ring Spot.",
            "2. Control Aphids: Manage aphid populations with insecticides or introduce natural predators.",
            "3. Sanitation Practices: Regularly inspect and remove infected plants to prevent virus spread.",
            "4. Crop Rotation: Rotate papaya with non-host crops to disrupt the virus life cycle.",
            "5. Physical Barriers: Use row covers or mesh to protect young plants from aphid infestation."
        ],
        
        "Scab Guava": [
            "1. Plant Resistant Varieties: Choose Resistant Cultivars: Opt for guava varieties that are resistant or less susceptible to scab.",
            "2. Proper Spacing and Pruning: Ensure Adequate Airflow: Space plants properly and regularly prune.",
            "3. Fungicide Application: Use effective fungicides during high-risk periods to prevent infection.",
            "4. Sanitation Practices: Remove fallen leaves and fruit regularly to reduce pathogen reservoirs.",
            "5. Water Management: Avoid overhead irrigation to reduce leaf wetness."
        ],
        "Styler and Root Guava": [
            "1.Improve Soil Drainage: Plant in well-draining soil to prevent water accumulation. Raised beds can enhance drainage.",
            "2.Use Disease-Resistant Varieties: Choose resistant varieties like 'Allahabad Safeda' to minimize root rot risk.",
            "3.Proper Irrigation Practices: Avoid overwatering; use drip irrigation for consistent moisture without saturation.",
            "4.Soil Health Management: Add compost to improve soil structure and promote healthy roots.",
            "5.Regular Monitoring and Sanitation: Inspect for root rot regularly and remove infected plants to prevent spread."
        ]
    }
    return recommendations.get(disease_class, ["No recommendations available."])
