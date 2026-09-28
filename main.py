items = [
    {
        "name": "Python Programming Course",
        "category": "Technology",
        "tags": ["python", "programming", "coding", "ai"]
    },
    {
        "name": "Machine Learning Course",
        "category": "Technology",
        "tags": ["machine learning", "ai", "python", "data"]
    },
    {
        "name": "Data Science Course",
        "category": "Technology",
        "tags": ["data", "python", "statistics", "machine learning"]
    },
    {
        "name": "Web Development Course",
        "category": "Technology",
        "tags": ["html", "css", "javascript", "web"]
    },
    {
        "name": "Graphic Design Course",
        "category": "Design",
        "tags": ["design", "graphics", "photoshop", "creative"]
    },
    {
        "name": "Digital Marketing Course",
        "category": "Marketing",
        "tags": ["marketing", "social media", "advertising", "business"]
    },
    {
        "name": "Business Management Course",
        "category": "Business",
        "tags": ["business", "management", "leadership", "marketing"]
    }
]


def calculate_similarity(user_preferences, item_tags):
    matches = 0

    for preference in user_preferences:
        if preference.lower() in [tag.lower() for tag in item_tags]:
            matches += 1

    if len(user_preferences) == 0:
        return 0

    return matches / len(user_preferences)


def recommend_items(user_preferences):
    recommendations = []

    for item in items:
        score = calculate_similarity(
            user_preferences,
            item["tags"]
        )

        if score > 0:
            recommendations.append(
                {
                    "name": item["name"],
                    "category": item["category"],
                    "score": score
                }
            )

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations


print("=" * 50)
print("       AI RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nEnter your interests.")
print("Example: python, ai, data")

user_input = input("\nYour interests: ")

user_preferences = [
    preference.strip().lower()
    for preference in user_input.split(",")
    if preference.strip()
]

recommendations = recommend_items(user_preferences)

print("\n" + "=" * 50)
print("RECOMMENDED ITEMS")
print("=" * 50)

if recommendations:
    for index, recommendation in enumerate(recommendations, start=1):
        percentage = recommendation["score"] * 100

        print(
            f"{index}. {recommendation['name']}"
        )
        print(
            f"   Category: {recommendation['category']}"
        )
        print(
            f"   Similarity Score: {percentage:.0f}%"
        )
        print()

else:
    print("No matching recommendations found.")

print("=" * 50)
print("Thank you for using the AI Recommendation System!")