import { useMutation } from "@tanstack/react-query";
import { api } from "../../../lib/http";
import type { Pipeline, ParseResult } from "../types";


export function useParsePipeline() {
    return useMutation({
        mutationFn: (p: Pipeline) => api<ParseResult>("/api/workflows/parse", {
            method: "POST",
            body: JSON.stringify(p),
        }),
    });
}