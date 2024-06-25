import HeaderB from '../components/HeaderB'
import Titulo from '../components/Titulo'
import CardListFunc from '@/components/CardListFunc'
import { useState, useEffect } from 'react'
import { getFuncionarios } from '@/service/apiReqRes'


export default function funcionarios() {
    const [funcionarios, setUsers] = useState([])

    async function buscaFuncionarios() {
        try {
            const data = await getFuncionarios()
            console.log(data)
            setUsers(data)
        }  catch (error) {
            console.error('Erro ao busca funcionário:', error)
        }
    }

    useEffect(() => {
        buscaFuncionarios()
        const atualiza = setInterval(buscaFuncionarios, 5000)
        return function () {
            clearInterval(atualiza)
        }
    }, [])

    return (
        <>
            <HeaderB title="Team"/>
            <Titulo texto="Conheça nossos funcionários!"/>
            <CardListFunc funcionarios={funcionarios} />
        </>
    )
}