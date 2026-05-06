const API_URL = "http://localhost:8000/api/drinks/";

export async function getDrinks() {
  const response = await fetch(API_URL, {
    headers: {
      Accept: "application/json",
    },
  });

  if (!response.ok) {
    throw new Error("Failed to fetch drinks");
  }

  return response.json();
}
