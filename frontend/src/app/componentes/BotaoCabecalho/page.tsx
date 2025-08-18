import Link from "next/link";
import './BotaoCabecalho.css';

const BotaoCabecalho = () => {
    return (
        <div className="botoes-container">
            <button className="botao">Perfil</button>
            <button className="botao">Configurações</button>
            
            <Link href="/login">
                <button className="botao">Login</button>
            </Link>

            <Link href="/cadastro">
                <button className="botao">Cadastro</button>
            </Link>
        </div>
    );
};

export default BotaoCabecalho;
