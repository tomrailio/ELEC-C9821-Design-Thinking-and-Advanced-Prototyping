import { serve } from "https://deno.land/std@0.140.0/http/server.ts";

const FILE_URL = new URL("./video.webm", import.meta.url).href;

serve(async () => {
  const resp = await fetch(FILE_URL);
  return new Response(resp.body, {
    headers: {
      "content-type": "video/webm",
    },
  });
});