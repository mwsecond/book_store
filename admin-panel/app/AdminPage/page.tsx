"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function AdminPage() {
  const router = useRouter();

  const [titulo, setTitulo] = useState("");
  const [autor, setAutor] = useState("");
  const [sinopse, setSinopse] = useState("");
  const [imagem, setImagem] = useState("");
  const [mensagem, setMensagem] = useState("");

  // Protege a rota
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) router.push("/login");
  }, [router]);

  // Envia dados para o backend
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const token = localStorage.getItem("token");

    if (!token) {
      router.push("/login");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/livros", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          titulo,
          autor,
          sinopse,
          imagem,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        setMensagem(data.message || "Erro ao cadastrar livro");
        return;
      }

      setMensagem("Livro cadastrado com sucesso!");
      setTitulo("");
      setAutor("");
      setSinopse("");
      setImagem("");

    } catch (error) {
      setMensagem("Erro de conexão com o servidor");
    }
  };

  return (
    <div>
      <h1>Painel Administrativo</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Título</label>
          <input value={titulo} onChange={e => setTitulo(e.target.value)} />
        </div>

        <div>
          <label>Autor</label>
          <input value={autor} onChange={e => setAutor(e.target.value)} />
        </div>

        <div>
          <label>Sinopse</label>
          <textarea value={sinopse} onChange={e => setSinopse(e.target.value)} />
        </div>

        <div>
          <label>Imagem (URL)</label>
          <input value={imagem} onChange={e => setImagem(e.target.value)} />
        </div>

        <button type="submit">Cadastrar Livro</button>
      </form>

      {mensagem && <p>{mensagem}</p>}
    </div>
  );
}
