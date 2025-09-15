import React from 'react';
import { useAuth } from '../context/AuthContext';
import { LogOut, User, Shield } from 'lucide-react';

const DashboardPage: React.FC = () => {
  const { user, logout } = useAuth();

  const handleLogout = () => {
    logout();
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <div className="flex items-center">
                <Shield className="h-8 w-8 text-blue-600" />
                <span className="ml-2 text-xl font-semibold text-gray-900">
                  Auth System
                </span>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <div className="flex items-center text-sm text-gray-700">
                <User className="h-4 w-4 mr-2" />
                {user?.username}
              </div>
              <button
                onClick={handleLogout}
                className="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
              >
                <LogOut className="h-4 w-4 mr-2" />
                Logout
              </button>
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <div className="bg-white overflow-hidden shadow rounded-lg">
            <div className="px-4 py-5 sm:p-6">
              <h1 className="text-2xl font-bold text-gray-900 mb-4">
                Welcome to your Dashboard!
              </h1>
              <p className="text-gray-600 mb-6">
                You have successfully logged in to the authentication system.
              </p>

              <div className="bg-blue-50 border border-blue-200 rounded-md p-4">
                <h3 className="text-lg font-medium text-blue-900 mb-2">
                  User Information
                </h3>
                <div className="space-y-2 text-sm">
                  <p>
                    <span className="font-medium text-blue-800">User:</span>{' '}
                    <span className="text-blue-700">{user?.username}</span>
                  </p>
                  {user?.first_name && (
                    <p>
                      <span className="font-medium text-blue-800">First Name:</span>{' '}
                      <span className="text-blue-700">{user.first_name}</span>
                    </p>
                  )}
                  {user?.last_name && (
                    <p>
                      <span className="font-medium text-blue-800">Last Name:</span>{' '}
                      <span className="text-blue-700">{user.last_name}</span>
                    </p>
                  )}
                  <p>
                    <span className="font-medium text-blue-800">User ID:</span>{' '}
                    <span className="text-blue-700">{user?.id}</span>
                  </p>
                </div>
              </div>

              <div className="mt-6 bg-green-50 border border-green-200 rounded-md p-4">
                <h3 className="text-lg font-medium text-green-900 mb-2">
                  Authentication Status
                </h3>
                <p className="text-sm text-green-700">
                  ✅ You are successfully authenticated with JWT tokens
                </p>
                <p className="text-sm text-green-700 mt-1">
                  🔒 Your session is secure and will automatically refresh
                </p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DashboardPage;