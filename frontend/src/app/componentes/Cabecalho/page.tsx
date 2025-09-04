import "./Cabecalho.css";
import BotaoCabecalho from "../BotaoCabecalho/page";
import Pesquisa from "../Pesquisa/page";
const Cabecalho = () => {
  // JSX
  return (
    <div>
      <header className="cabecalho">
        <img src="./Cabecalho_img/logoescrito.png" alt="" />
        <BotaoCabecalho></BotaoCabecalho>
      </header>
      <div>
        <Pesquisa></Pesquisa>
      </div>
    </div>
  );
};
export default Cabecalho;
