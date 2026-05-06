import DrinkCard from "../components/DrinkCard";
import { getDrinks } from "../services/drinkService";
import { useEffect, useState } from "react";

export default function DrinkListPage() {
  const [drinks, setDrinks] = useState([]);

  useEffect(() => {
    async function fetchDrinks() {
      try {
        const data = await getDrinks();
        console.log(data);
        setDrinks(data);
      } catch (error) {
        console.error("Error fetching drinks:", error);
      }
    }

    fetchDrinks();
  }, []);

  return (
    <div>
      {drinks.map((drink) => (
        <DrinkCard key={drink.id} drink={drink} />
      ))}
    </div>
  );
}
