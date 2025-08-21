import "./login.css"
import Link from "next/link";

const TelaLogin = () => {
  return (
    <div className="container">
      <div className="cabecalho-login">
        <Link href="/">
          <img src="./Cabecalho_img/logoescrito.png" alt="Logo" />
        </Link>
      </div>
      <div className="tela-login-container">
        <form className="folha">
          <h3>Login</h3>

          <div className="campo">
            <label htmlFor="email">E-mail do Cliente:</label>
            <input
              type="email"
              id="email"
              placeholder="name@flowbite.com"
              required
            />
          </div>

          <div className="campo">
            <label htmlFor="password">Senha de Acesso:</label>
            <input type="password" id="password" required />
          </div>

          <button type="submit" className="botao-login">
            Entrar
          </button>
        <p className="texto-cadastro">
          Não possui conta?{" "}
          <a href="/cadastro" className="link-cadastro">
            Cadastre-se
          </a>
        </p>
        </form>

      </div>
    </div>
  );
};

export default TelaLogin;
