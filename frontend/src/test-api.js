// Simple test script to verify API connection
const testLogin = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/accounts/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: 'testuser2',
        password: 'test2pass123'
      })
    });

    const data = await response.json();
    console.log('Response status:', response.status);
    console.log('Response data:', data);

    if (response.ok) {
      console.log('✅ Login successful!');
      console.log('Access token:', data.access);
      console.log('Refresh token:', data.refresh);
    } else {
      console.log('❌ Login failed:', data);
    }
  } catch (error) {
    console.error('❌ Network error:', error);
  }
};

testLogin();