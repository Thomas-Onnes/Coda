export function DrinkCard({ drink }) {
  return (
    <div>
      <h2>{drink.name}</h2>
      <p>{drink.brand}</p>
      <p>{drink.rating}</p>
    </div>
  );
}

export default DrinkCard;
