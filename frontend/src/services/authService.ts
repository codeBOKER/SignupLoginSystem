import api from './api';
import { LoginCredentials, SignupCredentials, AuthResponse, User } from '../types/auth';

export const authService = {
  async login(credentials: LoginCredentials): Promise<AuthResponse> {
    const response = await api.post('/accounts/token/', credentials);
    return response.data;
  },

  async signup(credentials: SignupCredentials): Promise<AuthResponse> {
    const response = await api.post('/accounts/', credentials);
    return response.data;
  },

  async resetPassword(email: string): Promise<void> {
    await api.post('/accounts/password-reset/', { email });
  },

  async getCurrentUser(): Promise<User> {
    const response = await api.get('/accounts/me/');
    return response.data;
  },

  logout(): void {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
  },

  isAuthenticated(): boolean {
    return !!localStorage.getItem('access_token');
  },
};