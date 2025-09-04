import "./Lancamento.css";

const Lancamento = () => {
  return (
    <div>
        <div className="titulo">
            Confira os lançamentos do gereno -GENERO-
        </div>
      <div className="cards-container">
        <div className="card-lancamento">
          <div className="card-conteudo">
            <h1>Item Numero 000*</h1>
            <div className="img-card">
              <img src="./Cabecalho_img/logoescrito.png" alt="" />
            </div>
            <h3>breve descrição*</h3>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Lancamento;
