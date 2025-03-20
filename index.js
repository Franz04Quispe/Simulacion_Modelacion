// Modal para la carga del codigo en Python
const loading = document.getElementById('loading');
addEventListener('py:ready', () => loading.close());
loading.showModal();