import Text.Read

fib :: Int -> Int
fib n
    | n < 0     = 0
    | n == 0    = 1
    | otherwise = (fib (n - 1)) + (fib (n - 2))

razondeOro :: Int -> Float -> Int -> Float
razondeOro currentsegmento previousdiametro totalsegmentos
    | currentsegmento <= 0 || currentsegmento > totalsegmentos =
        0
    | currentsegmento == totalsegmentos =
        previousdiametro
    | otherwise =
        previousdiametro * fromIntegral (fib currentsegmento) / fromIntegral (fib (currentsegmento + 1))

ciclo :: Int -> Float -> Int -> IO()
ciclo currentsegmento previousdiametro totalsegmentos
    | currentsegmento <= 0    = return ()
    | otherwise = do
        let diametro = razondeOro currentsegmento previousdiametro totalsegmentos
        putStrLn $ "Diametro del segmentoo " ++ show currentsegmento ++ ": " ++ show diametro
        ciclo (currentsegmento - 1) diametro totalsegmentos

validarInt :: String -> IO Int
validarInt prompt = do
    putStr prompt
    input <- getLine
    case readMaybe input :: Maybe Int of
        Just x -> return x
        Nothing -> putStrLn "\n[Error] Numero invalido, por favor intentelo denuevo." >> validarInt prompt

validarFloat :: String -> IO Float
validarFloat prompt = do
    putStr prompt
    input <- getLine
    case readMaybe input :: Maybe Float of
        Just x -> return x
        Nothing -> putStrLn "\n[Error] Numero invalido, por favor intentelo denuevo." >> validarFloat prompt

main = do
    segmento <- validarInt "Por favor especifique el numero de segmento deseado: "
    diametro <- validarFloat "Por favor especifique el diametro del segmento actual: "
    putStrLn ""
    ciclo segmento diametro segmento
