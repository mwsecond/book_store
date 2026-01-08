"use client";
import "./Lancamento.css";
import { useEffect, useState } from "react";
import axios from "axios";

// 🧩 Define o formato dos dados que vêm do backend
interface Livro {
  id: number;
  titulo: string;
  sinopse: string;
  imagem?: string; // opcional
}

const Lancamento = () => {
  // ✅ Agora o TypeScript sabe que "livros" é uma lista de objetos "Livro"
  const [livros, setLivros] = useState<Livro[]>([]);

  useEffect(() => {
    const buscarLivros = async () => {
      try {
        const resposta = await axios.get<Livro[]>("http://127.0.0.1:5000/livros");
        setLivros(resposta.data);
      } catch (erro) {
        console.error("Erro ao buscar livros:", erro);
      }
    };

    buscarLivros();
  }, []);

  return (
    <div>
      <div className="titulo">Lançamentos Recentes</div>

      <div className="cards-container">
        {livros.length > 0 ? (
          livros.map((livro) => (
            <div className="card-lancamento" key={livro.id}>
              <div className="card-conteudo">
                <div className="img-card">
                  <img
                    src={livro.imagem ? livro.imagem : "./Cabecalho_img/logoescrito.png"}
                    alt={livro.titulo}
                  />
                </div>
                <div className="descricao">
                  <h1>{livro.titulo}</h1>
                  <h3>{livro.sinopse}</h3>
                </div>
              </div>
            </div>
          ))
        ) : (
          <p style={{ color: "black", textAlign: "center" }}>Nenhum livro encontrado.</p>
        )}
      </div>
    </div>
  );
};

export default Lancamento;
