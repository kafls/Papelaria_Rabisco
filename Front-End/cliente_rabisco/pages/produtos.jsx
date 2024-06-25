import HeaderB from '../components/HeaderB'
import Titulo from '../components/Titulo'
import CardList from '@/components/CardList'
import { useState, useEffect } from 'react'
import { getProdutos } from '@/service/apiRabisco'


export default function produtos() {
    const [produtos, setProdutos] = useState([])

    async function buscaProdutos() {
        try {
            const data = await getProdutos()
            console.log(data)
            setProdutos(data)
        }  catch (error) {
            console.error('Erro ao busca produto:', error)
        }
    }

    useEffect(() => {
        buscaProdutos()
        const atualiza = setInterval(buscaProdutos, 5000)
        return function () {
            clearInterval(atualiza)
        }
    }, [])

    return (
        <>
            <HeaderB title="Produtos"/>
            <Titulo texto="Conheça nossos produtos!"/>
            <CardList produtos={produtos} />
        </>
    )
}