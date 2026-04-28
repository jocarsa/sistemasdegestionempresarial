const chatArea = document.getElementById("chatArea");
const preguntaEl = document.getElementById("pregunta");
const btnPreguntar = document.getElementById("btnPreguntar");
const clearChatBtn = document.getElementById("clearChatBtn");

const userMessageTemplate = document.getElementById("userMessageTemplate");
const assistantMessageTemplate = document.getElementById("assistantMessageTemplate");
const loadingTemplate = document.getElementById("loadingTemplate");

const quickPromptButtons = document.querySelectorAll(".quick-prompt");

let loadingNode = null;

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text ?? "";
    return div.innerHTML;
}

function autoResizeTextarea() {
    preguntaEl.style.height = "auto";
    preguntaEl.style.height = Math.min(preguntaEl.scrollHeight, 220) + "px";
}

function scrollChatToBottom(smooth = true) {
    chatArea.scrollTo({
        top: chatArea.scrollHeight,
        behavior: smooth ? "smooth" : "auto"
    });
}

function removeWelcomeCard() {
    const welcomeCard = chatArea.querySelector(".welcome-card");
    if (welcomeCard) {
        welcomeCard.remove();
    }
}

function addUserMessage(text) {
    removeWelcomeCard();

    const node = userMessageTemplate.content.firstElementChild.cloneNode(true);
    node.querySelector(".message-text").textContent = text;
    chatArea.appendChild(node);
    scrollChatToBottom();
}

function addLoadingMessage() {
    removeWelcomeCard();

    loadingNode = loadingTemplate.content.firstElementChild.cloneNode(true);
    chatArea.appendChild(loadingNode);
    scrollChatToBottom();
}

function removeLoadingMessage() {
    if (loadingNode && loadingNode.parentNode) {
        loadingNode.parentNode.removeChild(loadingNode);
    }
    loadingNode = null;
}

function createChip(text, className = "query-chip") {
    const span = document.createElement("span");
    span.className = className;
    span.textContent = text;
    return span;
}

function buildSourceCard(fragmento, index) {
    const meta = fragmento.metadata || {};

    const wrapper = document.createElement("div");
    wrapper.className = "source-card";

    const metaBar = document.createElement("div");
    metaBar.className = "source-meta";

    const chips = [
        `#${index + 1}`,
        meta.ciclo ? `Ciclo: ${meta.ciclo}` : null,
        meta.doc_type ? `Tipo: ${meta.doc_type}` : null,
        meta.articulo_num ? `Artículo ${meta.articulo_num}` : null,
        meta.capitulo && meta.capitulo !== "sin_capitulo" ? meta.capitulo : null,
        fragmento.source_collection ? `Colección: ${fragmento.source_collection}` : null,
        fragmento.score !== undefined ? `Score: ${Number(fragmento.score).toFixed(2)}` : null
    ].filter(Boolean);

    chips.forEach(chip => metaBar.appendChild(createChip(chip, "meta-chip")));

    const body = document.createElement("div");
    body.className = "source-body";
    body.textContent = fragmento.document || "";

    wrapper.appendChild(metaBar);
    wrapper.appendChild(body);

    return wrapper;
}

function addAssistantMessage(responseText, fragmentos = [], queriesUsadas = []) {
    const node = assistantMessageTemplate.content.firstElementChild.cloneNode(true);

    const responseEl = node.querySelector(".assistant-response");
    const toggleBtn = node.querySelector(".toggle-sources-btn");
    const metaPanel = node.querySelector(".meta-panel");
    const queriesList = node.querySelector(".queries-list");
    const sourcesList = node.querySelector(".sources-list");

    responseEl.textContent = responseText || "";

    if (!queriesUsadas.length && !fragmentos.length) {
        toggleBtn.style.display = "none";
    }

    queriesUsadas.forEach(q => {
        queriesList.appendChild(createChip(q));
    });

    fragmentos.forEach((fragmento, i) => {
        sourcesList.appendChild(buildSourceCard(fragmento, i));
    });

    toggleBtn.addEventListener("click", () => {
        const isHidden = metaPanel.classList.contains("hidden");
        metaPanel.classList.toggle("hidden");
        toggleBtn.textContent = isHidden ? "Ocultar fuentes" : "Ver fuentes";
        if (isHidden) {
            setTimeout(() => scrollChatToBottom(), 120);
        }
    });

    chatArea.appendChild(node);
    scrollChatToBottom();
}

function addErrorMessage(errorText) {
    addAssistantMessage(errorText || "Se ha producido un error.");
}

async function preguntar() {
    const pregunta = preguntaEl.value.trim();

    if (!pregunta) {
        preguntaEl.focus();
        return;
    }

    addUserMessage(pregunta);
    preguntaEl.value = "";
    autoResizeTextarea();

    btnPreguntar.disabled = true;
    preguntaEl.disabled = true;
    addLoadingMessage();

    try {
        const response = await fetch("/api/preguntar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ pregunta })
        });

        const data = await response.json();
        removeLoadingMessage();

        if (!response.ok || !data.ok) {
            addErrorMessage(data.error || "No se ha podido completar la consulta.");
            return;
        }

        addAssistantMessage(
            data.respuesta || "",
            data.fragmentos || [],
            data.queries_usadas || []
        );
    } catch (error) {
        removeLoadingMessage();
        addErrorMessage("Error de red: " + String(error));
    } finally {
        btnPreguntar.disabled = false;
        preguntaEl.disabled = false;
        preguntaEl.focus();
    }
}

btnPreguntar.addEventListener("click", preguntar);

preguntaEl.addEventListener("input", autoResizeTextarea);

preguntaEl.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        preguntar();
    }
});

clearChatBtn.addEventListener("click", () => {
    chatArea.innerHTML = `
        <div class="welcome-card">
            <div class="welcome-badge">Normativa FP</div>
            <h3>Haz una consulta sobre ciclos formativos</h3>
            <p>
                Puedes preguntar por duración, competencias, artículos, módulos profesionales,
                entorno profesional, cualificaciones o diferencias entre ciclos.
            </p>
        </div>
    `;
    preguntaEl.focus();
});

quickPromptButtons.forEach(button => {
    button.addEventListener("click", () => {
        preguntaEl.value = button.dataset.prompt || "";
        autoResizeTextarea();
        preguntaEl.focus();
    });
});

autoResizeTextarea();
