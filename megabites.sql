--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: addresses; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE addresses (
    add_id integer NOT NULL,
    lat double precision NOT NULL,
    lng double precision NOT NULL,
    formatted_add character varying(200)
);


ALTER TABLE addresses OWNER TO vagrant;

--
-- Name: addresses_add_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE addresses_add_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE addresses_add_id_seq OWNER TO vagrant;

--
-- Name: addresses_add_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE addresses_add_id_seq OWNED BY addresses.add_id;


--
-- Name: donors; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE donors (
    donor_id integer NOT NULL,
    name character varying(100),
    email character varying(75) NOT NULL,
    password character varying(100) NOT NULL,
    add_id integer,
    phone_number character varying(100)
);


ALTER TABLE donors OWNER TO vagrant;

--
-- Name: donors_donor_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE donors_donor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE donors_donor_id_seq OWNER TO vagrant;

--
-- Name: donors_donor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE donors_donor_id_seq OWNED BY donors.donor_id;


--
-- Name: foods; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE foods (
    food_id integer NOT NULL,
    donor_id integer NOT NULL,
    receiver_id integer,
    name character varying(50) NOT NULL,
    date_of_expiration timestamp without time zone NOT NULL,
    servings integer NOT NULL,
    prepared boolean NOT NULL,
    gluten boolean NOT NULL,
    refrigerated boolean NOT NULL,
    nuts boolean NOT NULL,
    dairy boolean NOT NULL,
    vegetarian boolean NOT NULL
);


ALTER TABLE foods OWNER TO vagrant;

--
-- Name: foods_food_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE foods_food_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE foods_food_id_seq OWNER TO vagrant;

--
-- Name: foods_food_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE foods_food_id_seq OWNED BY foods.food_id;


--
-- Name: receivers; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE receivers (
    receiver_id integer NOT NULL,
    name character varying(100),
    email character varying(75) NOT NULL,
    password character varying(100) NOT NULL,
    add_id integer,
    phone_number character varying(100)
);


ALTER TABLE receivers OWNER TO vagrant;

--
-- Name: receivers_receiver_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE receivers_receiver_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE receivers_receiver_id_seq OWNER TO vagrant;

--
-- Name: receivers_receiver_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE receivers_receiver_id_seq OWNED BY receivers.receiver_id;


--
-- Name: add_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY addresses ALTER COLUMN add_id SET DEFAULT nextval('addresses_add_id_seq'::regclass);


--
-- Name: donor_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY donors ALTER COLUMN donor_id SET DEFAULT nextval('donors_donor_id_seq'::regclass);


--
-- Name: food_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY foods ALTER COLUMN food_id SET DEFAULT nextval('foods_food_id_seq'::regclass);


--
-- Name: receiver_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY receivers ALTER COLUMN receiver_id SET DEFAULT nextval('receivers_receiver_id_seq'::regclass);


--
-- Data for Name: addresses; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY addresses (add_id, lat, lng, formatted_add) FROM stdin;
\.


--
-- Name: addresses_add_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('addresses_add_id_seq', 1, false);


--
-- Data for Name: donors; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY donors (donor_id, name, email, password, add_id, phone_number) FROM stdin;
\.


--
-- Name: donors_donor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('donors_donor_id_seq', 1, false);


--
-- Data for Name: foods; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY foods (food_id, donor_id, receiver_id, name, date_of_expiration, servings, prepared, gluten, refrigerated, nuts, dairy, vegetarian) FROM stdin;
\.


--
-- Name: foods_food_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('foods_food_id_seq', 1, false);


--
-- Data for Name: receivers; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY receivers (receiver_id, name, email, password, add_id, phone_number) FROM stdin;
\.


--
-- Name: receivers_receiver_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('receivers_receiver_id_seq', 1, false);


--
-- Name: addresses_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY addresses
    ADD CONSTRAINT addresses_pkey PRIMARY KEY (add_id);


--
-- Name: donors_email_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY donors
    ADD CONSTRAINT donors_email_key UNIQUE (email);


--
-- Name: donors_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY donors
    ADD CONSTRAINT donors_pkey PRIMARY KEY (donor_id);


--
-- Name: foods_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY foods
    ADD CONSTRAINT foods_pkey PRIMARY KEY (food_id);


--
-- Name: receivers_email_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY receivers
    ADD CONSTRAINT receivers_email_key UNIQUE (email);


--
-- Name: receivers_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY receivers
    ADD CONSTRAINT receivers_pkey PRIMARY KEY (receiver_id);


--
-- Name: donors_add_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY donors
    ADD CONSTRAINT donors_add_id_fkey FOREIGN KEY (add_id) REFERENCES addresses(add_id);


--
-- Name: foods_donor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY foods
    ADD CONSTRAINT foods_donor_id_fkey FOREIGN KEY (donor_id) REFERENCES donors(donor_id);


--
-- Name: foods_receiver_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY foods
    ADD CONSTRAINT foods_receiver_id_fkey FOREIGN KEY (receiver_id) REFERENCES receivers(receiver_id);


--
-- Name: receivers_add_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY receivers
    ADD CONSTRAINT receivers_add_id_fkey FOREIGN KEY (add_id) REFERENCES addresses(add_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

