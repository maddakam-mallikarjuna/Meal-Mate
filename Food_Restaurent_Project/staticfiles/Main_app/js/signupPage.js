const table = document.querySelector("tbody");

const textara = document.querySelector("#Address");
const textara_label = document.querySelector(".Address");

if (!table) {
    console.error("No <tbody> found!");
} else {
    const rows = table.querySelectorAll("tr");

    let labels = [];
    let inputs = [];

    rows.forEach((row) => {
        const input = row.querySelector("input");
        const label = row.querySelector("label");

        if (input) inputs.push(input);
        if (label) labels.push(label);
    });

    inputs.forEach((input, index) => {
        input.addEventListener("focus", () => {
            labels[index].style.color = "black"; 
        });

        input.addEventListener("blur", () => {
            labels[index].style.color = "";
        });
    });
}

textara.addEventListener("focus", () => {
    textara_label.style.color = "black";
});

textara.addEventListener("blur", () => {
    textara_label.style.color = "";
});
