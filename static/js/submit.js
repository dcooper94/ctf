
async function submitFlag(flag) {
    const response = await fetch('/submit', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: 'flag=' + encodeURIComponent(flag)
    });
    const text = await response.text();
    alert(text);
}
