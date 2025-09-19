import piatti from "./piatti";

function Menu() {
    return (
        <ul>
            {
                piatti.map((p) => (
                    <li key={p.id}>nome: {p.nome} prezzo: {p.prezzo}</li>
                ))}
        </ul>
    );
}

export default Menu;