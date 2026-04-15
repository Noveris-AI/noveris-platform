import type { AxiosInstance, AxiosResponse } from "axios";

interface ApiError {
  code: string;
  message: string;
  detail?: Record<string, unknown>;
}

export function setupInterceptors(client: AxiosInstance) {
  client.interceptors.response.use(
    (response: AxiosResponse) => response,
    (error) => {
      if (error.response?.status === 401) {
        window.location.href = "/login";
        return Promise.reject(error);
      }

      const data = error.response?.data as ApiError | undefined;
      if (data?.code && data?.message) {
        // structured NavimaError
        return Promise.reject(data);
      }

      return Promise.reject(error);
    },
  );
}
