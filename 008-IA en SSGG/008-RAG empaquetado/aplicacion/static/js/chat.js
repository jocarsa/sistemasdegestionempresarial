document.addEventListener("DOMContentLoaded", function () {

  const input = document.getElementById("consulta");
  const mensajes = document.getElementById("mensajes");

  input.addEventListener("keydown", async function (e) {

    if (e.key === "Enter") {

      e.preventDefault();

      const texto = input.value.trim();

      if (!texto) {
        return;
      }

      // mensaje usuario

      const usuario = document.createElement("article");
      usuario.textContent = texto;

      mensajes.appendChild(usuario);

      input.value = "";

      mensajes.scrollTop = mensajes.scrollHeight;

      try {

        const response = await fetch("/api/chat", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            consulta: texto
          })
        });

        const data = await response.json();

        // respuesta IA

        const ia = document.createElement("article");
        ia.textContent = data.respuesta;

        mensajes.appendChild(ia);

        mensajes.scrollTop = mensajes.scrollHeight;

      } catch (error) {

        const ia = document.createElement("article");
        ia.textContent = "Error conectando con el servidor.";

        mensajes.appendChild(ia);

      }

    }

  });

});