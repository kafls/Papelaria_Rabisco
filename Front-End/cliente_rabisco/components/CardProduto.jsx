export default function CardProduto(props) {
    return (
        
        <div className="card">
            <div className="col">
                <div className="card">
                <img src={`produtos/${props.nome}.png`} className="card-img-top" alt="..." onError={(e)=>e.target.src="produtos/placeholder.jpg"} style={{ height: '280px', objectFit: 'cover'}}/>
                <div className="card-body">
                    <h5 className="card-title">{props.nome}</h5>
                    <p className="card-text">{props.descricao}</p>
                    <a href="#" className="btn btn-primary">R$ {props.preco}</a>
                </div>
                <div className="card-footer">
                    <p className="card-text">{props.quantidade} unidade (s) em estoque</p>
                </div>
                </div>
            </div>
        </div>
    )
}
CardProduto.defaultProps = {
    nome: 'Produto',
    descricao: 'Descrição do produto',
    preco: 0,
    quantidade: 0
}

