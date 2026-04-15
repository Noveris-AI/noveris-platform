import { useEffect, useRef, useState } from "react";

export function useSse(url: string) {
  const [data, setData] = useState<string>("");
  const [error, setError] = useState<Error | null>(null);
  const eventSourceRef = useRef<EventSource | null>(null);

  useEffect(() => {
    const es = new EventSource(url, { withCredentials: true });
    eventSourceRef.current = es;

    es.onmessage = (event) => {
      setData(event.data);
    };

    es.onerror = () => {
      setError(new Error("SSE connection error"));
      es.close();
    };

    return () => {
      es.close();
    };
  }, [url]);

  return { data, error };
}
