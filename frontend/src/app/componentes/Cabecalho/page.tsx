import "./Cabecalho.css";
import Link from "next/link";

const Cabecalho = () => {
  // JSX
  return (
    <div>
      <header className="cabecalho">
        <Link href="/">
          <img src="/Cabecalho_img/logoescrito.png" alt="Logo" />
        </Link>
      </header>
      <div>
       
      </div>
    </div>
  );
};
export default Cabecalho;
