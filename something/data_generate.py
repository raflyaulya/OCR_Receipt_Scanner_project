from faker import Faker
import random
import pandas as pd

fake = Faker()
topics = ["sports", "tech", "politics", "health", "entertainment", "finance"]

data = []
total_rows = 50

for i in range(total_rows):
    data.append({
        "article_id": i + 1,
        "article_topic": random.choice(topics),
        "article_content": fake.paragraph(nb_sentences=5),
        # "article_content": fake.
    })

df = pd.DataFrame(data)
df.to_csv(f"data_rows{total_rows}.csv", index=False)
