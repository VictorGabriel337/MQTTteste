function ligarLed() {
    fetch('http://127.0.0.1:5000/ligar', {
        method: "POST"
    })
    .then(response => response.text())
    .then(data => {
        console.log("Resposta do servidor:", data);
        document.getElementById("status").innerText = "LED Ligado";
    })
    .catch(error => {
        console.error("Erro ao ligar o LED:", error);
    });
}

function desligarLed() {
    fetch('http://127.0.0.1:5000/desligar', {
        method: "POST"
    })
    .then(response => response.text())
    .then(data => {
        console.log("Resposta do servidor:", data);
        document.getElementById("status").innerText = "LED Desligado";
    })
    .catch(error => {
        console.error("Erro ao desligar o LED:", error);
    });
}
