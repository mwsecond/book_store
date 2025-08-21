import './Cabecalho.css'
import BotaoCabecalho from '../BotaoCabecalho/page'
import Pesquisa from '../Pesquisa/page'
const Cabecalho = () => {
    // JSX
    return (
        <header className="cabecalho">
        <img src="./Cabecalho_img/logoescrito.png" alt="" />
            <Pesquisa></Pesquisa>
            <BotaoCabecalho></BotaoCabecalho>

        </header>
    )
}
export default Cabecalho