import CardProduto from "./CardProduto"

export default function CardList(props){
    const {produtos} = props
    return(
        <div className="container my-2">
                <div className="row g-5">
                    {/* Estrutura de repetição map */}
                    {produtos.map(function (produto, index){
                        return(
                            <div className="col-12 col-sm-6 col-md-4 col-lg-3" key={index}>
                                <CardProduto
                                    nome={produto.nome}
                                    descricao={produto.descricao}
                                    preco={produto.preco}
                                    quantidade={produto.quantidade}
                                />
                            </div> 
                        )
                    })}

                </div>
            </div>
    )
}


