document.addEventListener('DOMContentLoaded', () => {
    const queryInput = document.getElementById('query-input');
    const submitBtn = document.getElementById('submit-btn');
    const responseOutput = document.getElementById('response-output');

    submitBtn.addEventListener('click', async () => {
        const query = queryInput.value.trim();
        if (!query) {
            alert('Please enter a query.');
            return;
        }

        try {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Processing...';
            responseOutput.textContent = 'Fetching response...';

            const response = await fetch('http://localhost:8000/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: query }),
            });

            if (!response.ok) {
                throw new Error('Failed to fetch response');
            }

            const data = await response.json();
            responseOutput.textContent = data.answer;
        } catch (error) {
            console.error('Error:', error);
            responseOutput.textContent = 'An error occurred while processing your query.';
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Submit Query';
        }
    });
});