async function loadPackPrices() {
const priceList = document.querySelector(".pack-price-list");

try {
    const response = await fetch("http://127.0.0.1:8000/api/pack-prices");

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
    }

    const packs = await response.json();

    priceList.innerHTML = "";

    packs.forEach((pack) => {
        const packCard = document.createElement("div");
        packCard.className = "pack-card";

        packCard.innerHTML = `
            <h3>${pack.set}</h3>
            <p>Standard Booster Pack</p>

            <p>
                Pack Price:
                <strong>$${pack.pack_price.toFixed(2)}</strong>
            </p>

            <p>
                Average Card Value:
                <strong>$${pack.average_card_value.toFixed(2)}</strong>
            </p>

            <p>
                Estimated Return:
                <strong>$${pack.estimated_return.toFixed(2)}</strong>
            </p>
        `;

        priceList.appendChild(packCard);
    });
} catch (error) {
    console.error("Failed to load pack prices:", error);

    priceList.innerHTML = `
        <p>Unable to load pack prices. Please try again later.</p>
    `;
}

}

loadPackPrices();
