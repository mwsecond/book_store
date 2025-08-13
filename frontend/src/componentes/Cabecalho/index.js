import './cabecalho.css'
import BotaoCabecalho from  '../BotaoCabecalho'
const Cabecalho = () => {
    // JSX
    return (
        <header className="cabecalho">
            <div>
            <img src="/Cabecalho_img/logoescrito.png" alt="Nome da Indietora (sem fundo)"/>
            </div>
            <BotaoCabecalho></BotaoCabecalho>
       
        </header>
    )
}
export default Cabecalho