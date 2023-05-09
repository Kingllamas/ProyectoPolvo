-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 09-05-2023 a las 13:04:19
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `polvos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clase_combustion_datos`
--

DROP TABLE IF EXISTS `clase_combustion_datos`;
CREATE TABLE IF NOT EXISTS `clase_combustion_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `hilera_polvo` varchar(50) DEFAULT NULL,
  `tiempo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clo_datos`
--

DROP TABLE IF EXISTS `clo_datos`;
CREATE TABLE IF NOT EXISTS `clo_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `concentracion_polvo` varchar(50) DEFAULT NULL,
  `concentracion_oxigeno` varchar(50) DEFAULT NULL,
  `peso_equivalente` varchar(50) DEFAULT NULL,
  `pm` varchar(50) DEFAULT NULL,
  `dpdt` varchar(50) DEFAULT NULL,
  `observaciones` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `emi_datos`
--

DROP TABLE IF EXISTS `emi_datos`;
CREATE TABLE IF NOT EXISTS `emi_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `concentracion` varchar(50) DEFAULT NULL,
  `energia` varchar(50) DEFAULT NULL,
  `retardo` varchar(50) DEFAULT NULL,
  `resultado` varchar(50) DEFAULT NULL,
  `observaciones` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresas`
--

DROP TABLE IF EXISTS `empresas`;
CREATE TABLE IF NOT EXISTS `empresas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `empresa` varchar(50) DEFAULT NULL,
  `subsidiaria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `empresas`
--

INSERT INTO `empresas` (`id`, `empresa`, `subsidiaria`) VALUES
(1, 'sadim', 'rouselt'),
(2, 'urike', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ensayos`
--

DROP TABLE IF EXISTS `ensayos`;
CREATE TABLE IF NOT EXISTS `ensayos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ensayo` varchar(50) DEFAULT NULL,
  `normativa` varchar(50) DEFAULT NULL,
  `procedimiento` varchar(50) DEFAULT NULL,
  `id_equipo1` varchar(50) DEFAULT NULL,
  `id_equipo2` varchar(50) DEFAULT NULL,
  `id_equipo3` varchar(50) DEFAULT NULL,
  `id_equipo4` varchar(50) DEFAULT NULL,
  `id_equipo5` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_equipo1` (`id_equipo1`),
  KEY `id_equipo2` (`id_equipo2`),
  KEY `id_equipo3` (`id_equipo3`),
  KEY `id_equipo4` (`id_equipo4`),
  KEY `id_equipo5` (`id_equipo5`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `ensayos`
--

INSERT INTO `ensayos` (`id`, `ensayo`, `normativa`, `procedimiento`, `id_equipo1`, `id_equipo2`, `id_equipo3`, `id_equipo4`, `id_equipo5`) VALUES
(1, 'tmicapa', 'UNE-EN ISO/IEC 80079-20-2:2016', 'POENS 551', NULL, NULL, NULL, NULL, NULL),
(2, 'tminube', 'UNE-EN ISO/IEC 80080-20-2:2016', 'POENS 552', NULL, NULL, NULL, NULL, NULL),
(3, 'EMI', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

DROP TABLE IF EXISTS `equipos`;
CREATE TABLE IF NOT EXISTS `equipos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `equipo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `humedad_datos`
--

DROP TABLE IF EXISTS `humedad_datos`;
CREATE TABLE IF NOT EXISTS `humedad_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `humedad` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lie_datos`
--

DROP TABLE IF EXISTS `lie_datos`;
CREATE TABLE IF NOT EXISTS `lie_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `concentracion` varchar(50) DEFAULT NULL,
  `peso_equivalente` varchar(50) DEFAULT NULL,
  `pex` varchar(50) DEFAULT NULL,
  `pm` varchar(50) DEFAULT NULL,
  `dpdt` varchar(50) DEFAULT NULL,
  `observaciones` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `molienda_datos`
--

DROP TABLE IF EXISTS `molienda_datos`;
CREATE TABLE IF NOT EXISTS `molienda_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `molienda` varchar(50) DEFAULT NULL,
  `equipo` varchar(50) DEFAULT NULL,
  `tiempo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `muestras`
--

DROP TABLE IF EXISTS `muestras`;
CREATE TABLE IF NOT EXISTS `muestras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `identificador` varchar(50) DEFAULT NULL,
  `numero` varchar(50) DEFAULT NULL,
  `expediente` varchar(50) DEFAULT NULL,
  `material` varchar(50) DEFAULT NULL,
  `peso` varchar(50) DEFAULT NULL,
  `id_procedencia` varchar(50) DEFAULT NULL,
  `fecha_recepcion` varchar(50) DEFAULT NULL,
  `fecha_fin` varchar(50) DEFAULT NULL,
  `id_empresa` int DEFAULT NULL,
  `realizado` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_procedencia` (`id_procedencia`),
  KEY `id_empresa` (`id_empresa`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `muestras`
--

INSERT INTO `muestras` (`id`, `identificador`, `numero`, `expediente`, `material`, `peso`, `id_procedencia`, `fecha_recepcion`, `fecha_fin`, `id_empresa`, `realizado`) VALUES
(1, 'sad', '26', '23,658 Q ', 'Polvo de lodo', '2', '1', '2022-03-06', '2021-03-21', 1, 'No'),
(2, 'sad', '27', '23,658 Q ', 'barro', '4', '1', '2020-03-06', '2024-03-21', 1, 'No'),
(3, 'URK', '1', '23,141 Q ', 'granalla', '3', '2', '2022-03-21', '2023-02-02', 2, 'yes');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `onu_n1_datos`
--

DROP TABLE IF EXISTS `onu_n1_datos`;
CREATE TABLE IF NOT EXISTS `onu_n1_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `numero_prueba` varchar(50) DEFAULT NULL,
  `t3` varchar(50) DEFAULT NULL,
  `rebasa` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `onu_n2_datos`
--

DROP TABLE IF EXISTS `onu_n2_datos`;
CREATE TABLE IF NOT EXISTS `onu_n2_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `numero_prueba` varchar(50) DEFAULT NULL,
  `inflamacion` varchar(50) DEFAULT NULL,
  `observaciones` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `onu_n4_datos`
--

DROP TABLE IF EXISTS `onu_n4_datos`;
CREATE TABLE IF NOT EXISTS `onu_n4_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `temperatura_estufa` varchar(50) DEFAULT NULL,
  `celda` varchar(50) DEFAULT NULL,
  `temperatura_maxima` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `onu_o1_datos`
--

DROP TABLE IF EXISTS `onu_o1_datos`;
CREATE TABLE IF NOT EXISTS `onu_o1_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `mezcla` varchar(50) DEFAULT NULL,
  `t1` varchar(50) DEFAULT NULL,
  `t2` varchar(50) DEFAULT NULL,
  `t3` varchar(50) DEFAULT NULL,
  `t4` varchar(50) DEFAULT NULL,
  `t5` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `procedencias`
--

DROP TABLE IF EXISTS `procedencias`;
CREATE TABLE IF NOT EXISTS `procedencias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `procedencia` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `procedencias`
--

INSERT INTO `procedencias` (`id`, `procedencia`) VALUES
(1, 'barcelona'),
(2, 'madrid');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rec_datos`
--

DROP TABLE IF EXISTS `rec_datos`;
CREATE TABLE IF NOT EXISTS `rec_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `tension` varchar(50) DEFAULT NULL,
  `duracion` varchar(50) DEFAULT NULL,
  `resistencia` varchar(50) DEFAULT NULL,
  `observaciones` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultados`
--

DROP TABLE IF EXISTS `resultados`;
CREATE TABLE IF NOT EXISTS `resultados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_muestras` varchar(50) DEFAULT NULL,
  `id_ensayos` varchar(50) DEFAULT NULL,
  `fecha` varchar(50) DEFAULT NULL,
  `humedad` varchar(50) DEFAULT NULL,
  `temperatura` varchar(50) DEFAULT NULL,
  `resultado` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_muestras` (`id_muestras`),
  KEY `id_ensayos` (`id_ensayos`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `resultados`
--

INSERT INTO `resultados` (`id`, `id_muestras`, `id_ensayos`, `fecha`, `humedad`, `temperatura`, `resultado`) VALUES
(1, '1', '1', '10/4/2023', '11%', '24', '340º'),
(2, '2', '1', '11/4/2023', '12%', '25', '380º'),
(3, '3', '1', '12/4/2023', '13%', '23', '440º'),
(4, '4', '1', '13/4/2023', '14%', '26', '480º'),
(5, '1', '2', '10/4/2023', '11%', '24', '380º'),
(6, '2', '2', '10/4/2023', '11%', '24', '380º'),
(7, '1', '3', '11/4/2023', '11%', '24', '100');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `secado_datos`
--

DROP TABLE IF EXISTS `secado_datos`;
CREATE TABLE IF NOT EXISTS `secado_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `secado` varchar(50) DEFAULT NULL,
  `estufa` varchar(50) DEFAULT NULL,
  `tiempo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `severidad_datos`
--

DROP TABLE IF EXISTS `severidad_datos`;
CREATE TABLE IF NOT EXISTS `severidad_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `concentracion` varchar(50) DEFAULT NULL,
  `pm_serie1` varchar(50) DEFAULT NULL,
  `pm_serie2` varchar(50) DEFAULT NULL,
  `pm_serie3` varchar(50) DEFAULT NULL,
  `dpdt_serie1` varchar(50) DEFAULT NULL,
  `dpdt_serie2` varchar(50) DEFAULT NULL,
  `dpdt_serie3` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tamizado_datos`
--

DROP TABLE IF EXISTS `tamizado_datos`;
CREATE TABLE IF NOT EXISTS `tamizado_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `tamizado` varchar(50) DEFAULT NULL,
  `equipo` varchar(50) DEFAULT NULL,
  `codigo` varchar(50) DEFAULT NULL,
  `tamaño` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tev_datos`
--

DROP TABLE IF EXISTS `tev_datos`;
CREATE TABLE IF NOT EXISTS `tev_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `temperatura_referencia` varchar(50) DEFAULT NULL,
  `temperatura_ensayo` varchar(50) DEFAULT NULL,
  `temperatura_maxima` varchar(50) DEFAULT NULL,
  `vapores_visibles` varchar(50) DEFAULT NULL,
  `inflama` varchar(50) DEFAULT NULL,
  `observaciones` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tmicapa_datos`
--

DROP TABLE IF EXISTS `tmicapa_datos`;
CREATE TABLE IF NOT EXISTS `tmicapa_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `temperatura` varchar(50) DEFAULT NULL,
  `temperatura_de_plato` varchar(50) DEFAULT NULL,
  `temperatura_maxima` varchar(50) DEFAULT NULL,
  `resultado_ignicion` varchar(50) DEFAULT NULL,
  `tiempo` varchar(50) DEFAULT NULL,
  `observaciones` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `tmicapa_datos`
--

INSERT INTO `tmicapa_datos` (`id`, `id_resultados`, `temperatura`, `temperatura_de_plato`, `temperatura_maxima`, `resultado_ignicion`, `tiempo`, `observaciones`) VALUES
(1, '1', '20', '100', '60', 'si', '10', 'ninguna'),
(2, '2', '21', '200', '70', 'no', '20', 'alguna'),
(3, '3', '22', '300', '80', 'si', '30', 'una'),
(4, '4', '23', '400', '90', 'no', '40', 'niuna'),
(5, '1', '20', '120', '60', 'si', '30', 'ninguna');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tminube_datos`
--

DROP TABLE IF EXISTS `tminube_datos`;
CREATE TABLE IF NOT EXISTS `tminube_datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_resultados` varchar(50) DEFAULT NULL,
  `temperatura` varchar(50) DEFAULT NULL,
  `peso` varchar(50) DEFAULT NULL,
  `presion` varchar(50) DEFAULT NULL,
  `resultado` varchar(50) DEFAULT NULL,
  `observaciones` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_resultados` (`id_resultados`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `contraseña` varchar(50) DEFAULT NULL,
  `siglas` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `email`, `contraseña`, `siglas`) VALUES
(1, 'sergio', NULL, 'pene', NULL),
(2, 'miguel', NULL, 'pene', NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
