--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
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


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO azomicrate;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO azomicrate;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO azomicrate;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO azomicrate;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO azomicrate;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO azomicrate;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO azomicrate;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO azomicrate;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO azomicrate;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO azomicrate;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO azomicrate;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO azomicrate;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO azomicrate;

--
-- Name: knox_authtoken; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.knox_authtoken (
    digest character varying(128) NOT NULL,
    salt character varying(16) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    expires timestamp with time zone,
    token_key character varying(8) NOT NULL
);


ALTER TABLE public.knox_authtoken OWNER TO azomicrate;

--
-- Name: medex_medicine; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.medex_medicine (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    name character varying(30) NOT NULL,
    mrp numeric(6,2) NOT NULL,
    quantity integer NOT NULL,
    "pricePerTablet" numeric(12,10) NOT NULL
);


ALTER TABLE public.medex_medicine OWNER TO azomicrate;

--
-- Name: medex_medicine_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.medex_medicine_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medex_medicine_id_seq OWNER TO azomicrate;

--
-- Name: medex_medicine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.medex_medicine_id_seq OWNED BY public.medex_medicine.id;


--
-- Name: medex_medicineofuser; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.medex_medicineofuser (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    "creditForMedicine" numeric(6,2),
    "expiryDate" date NOT NULL,
    "medicinePicture" character varying(100) NOT NULL,
    "expiryPicture" character varying(100) NOT NULL,
    "quantityOfMedicine" integer NOT NULL,
    "isSoldByPharmacist" boolean NOT NULL,
    "isAcceptedByPharmacist" boolean NOT NULL,
    "isRequested" boolean NOT NULL,
    medicine_id integer NOT NULL,
    pharmacist_id integer,
    user_id integer NOT NULL
);


ALTER TABLE public.medex_medicineofuser OWNER TO azomicrate;

--
-- Name: medex_medicineofuser_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.medex_medicineofuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medex_medicineofuser_id_seq OWNER TO azomicrate;

--
-- Name: medex_medicineofuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.medex_medicineofuser_id_seq OWNED BY public.medex_medicineofuser.id;


--
-- Name: medex_requestedmedicines; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.medex_requestedmedicines (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    "medicineRequested" character varying(20) NOT NULL,
    details character varying(50) NOT NULL,
    "isAccepted" boolean NOT NULL
);


ALTER TABLE public.medex_requestedmedicines OWNER TO azomicrate;

--
-- Name: medex_requestedmedicines_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.medex_requestedmedicines_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medex_requestedmedicines_id_seq OWNER TO azomicrate;

--
-- Name: medex_requestedmedicines_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.medex_requestedmedicines_id_seq OWNED BY public.medex_requestedmedicines.id;


--
-- Name: useraccounts_organisation; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.useraccounts_organisation (
    usermodel_ptr_id integer NOT NULL,
    latitude character varying(10000),
    longitude character varying(10000),
    "licenseOfOrganisation" character varying(100),
    "licenseNumber" character varying(15) NOT NULL
);


ALTER TABLE public.useraccounts_organisation OWNER TO azomicrate;

--
-- Name: useraccounts_pharamcy; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.useraccounts_pharamcy (
    usermodel_ptr_id integer NOT NULL,
    latitude character varying(10000),
    longitude character varying(10000),
    "licenseOfPharmacist" character varying(100),
    "licenseNumber" character varying(15) NOT NULL
);


ALTER TABLE public.useraccounts_pharamcy OWNER TO azomicrate;

--
-- Name: useraccounts_usermodel; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.useraccounts_usermodel (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    username character varying(80),
    email character varying(254) NOT NULL,
    "aadhaarNo" character varying(12) NOT NULL,
    address character varying(150) NOT NULL,
    "zipCode" character varying(6) NOT NULL,
    "totalCredits" numeric(6,2) NOT NULL,
    "phoneNumber" character varying(10) NOT NULL
);


ALTER TABLE public.useraccounts_usermodel OWNER TO azomicrate;

--
-- Name: useraccounts_usermodel_groups; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.useraccounts_usermodel_groups (
    id integer NOT NULL,
    usermodel_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.useraccounts_usermodel_groups OWNER TO azomicrate;

--
-- Name: useraccounts_usermodel_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.useraccounts_usermodel_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.useraccounts_usermodel_groups_id_seq OWNER TO azomicrate;

--
-- Name: useraccounts_usermodel_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.useraccounts_usermodel_groups_id_seq OWNED BY public.useraccounts_usermodel_groups.id;


--
-- Name: useraccounts_usermodel_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.useraccounts_usermodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.useraccounts_usermodel_id_seq OWNER TO azomicrate;

--
-- Name: useraccounts_usermodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.useraccounts_usermodel_id_seq OWNED BY public.useraccounts_usermodel.id;


--
-- Name: useraccounts_usermodel_user_permissions; Type: TABLE; Schema: public; Owner: azomicrate
--

CREATE TABLE public.useraccounts_usermodel_user_permissions (
    id integer NOT NULL,
    usermodel_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.useraccounts_usermodel_user_permissions OWNER TO azomicrate;

--
-- Name: useraccounts_usermodel_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: azomicrate
--

CREATE SEQUENCE public.useraccounts_usermodel_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.useraccounts_usermodel_user_permissions_id_seq OWNER TO azomicrate;

--
-- Name: useraccounts_usermodel_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: azomicrate
--

ALTER SEQUENCE public.useraccounts_usermodel_user_permissions_id_seq OWNED BY public.useraccounts_usermodel_user_permissions.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.medex_medicine ALTER COLUMN id SET DEFAULT nextval('public.medex_medicine_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.medex_medicineofuser ALTER COLUMN id SET DEFAULT nextval('public.medex_medicineofuser_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.medex_requestedmedicines ALTER COLUMN id SET DEFAULT nextval('public.medex_requestedmedicines_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel ALTER COLUMN id SET DEFAULT nextval('public.useraccounts_usermodel_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_groups ALTER COLUMN id SET DEFAULT nextval('public.useraccounts_usermodel_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.useraccounts_usermodel_user_permissions_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add group	2	add_group
6	Can change group	2	change_group
7	Can delete group	2	delete_group
8	Can view group	2	view_group
9	Can add permission	3	add_permission
10	Can change permission	3	change_permission
11	Can delete permission	3	delete_permission
12	Can view permission	3	view_permission
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add medicine of user	6	add_medicineofuser
22	Can change medicine of user	6	change_medicineofuser
23	Can delete medicine of user	6	delete_medicineofuser
24	Can view medicine of user	6	view_medicineofuser
25	Can add medicine	7	add_medicine
26	Can change medicine	7	change_medicine
27	Can delete medicine	7	delete_medicine
28	Can view medicine	7	view_medicine
29	Can add user	8	add_usermodel
30	Can change user	8	change_usermodel
31	Can delete user	8	delete_usermodel
32	Can view user	8	view_usermodel
33	Can add user	9	add_organisation
34	Can change user	9	change_organisation
35	Can delete user	9	delete_organisation
36	Can view user	9	view_organisation
37	Can add user	10	add_pharamcy
38	Can change user	10	change_pharamcy
39	Can delete user	10	delete_pharamcy
40	Can view user	10	view_pharamcy
41	Can add auth token	11	add_authtoken
42	Can change auth token	11	change_authtoken
43	Can delete auth token	11	delete_authtoken
44	Can view auth token	11	view_authtoken
45	Can add requested medicines	12	add_requestedmedicines
46	Can change requested medicines	12	change_requestedmedicines
47	Can delete requested medicines	12	delete_requestedmedicines
48	Can view requested medicines	12	view_requestedmedicines
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 48, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2019-03-03 00:16:20.723058+00	1	MedicineOfUser object (1)	1	[{"added": {}}]	6	1
2	2019-03-03 00:17:17.095274+00	2	MedicineOfUser object (2)	1	[{"added": {}}]	6	1
3	2019-03-03 00:17:29.331695+00	2	MedicineOfUser object (2)	2	[{"changed": {"fields": ["isAcceptedByPharmacist", "isRequested"]}}]	6	1
4	2019-03-03 00:20:15.774512+00	2	MedicineOfUser object (2)	2	[{"changed": {"fields": ["isAcceptedByPharmacist", "isRequested"]}}]	6	1
5	2019-03-03 00:20:22.157762+00	1	MedicineOfUser object (1)	2	[{"changed": {"fields": ["isAcceptedByPharmacist", "isRequested"]}}]	6	1
6	2019-03-03 00:21:58.241969+00	3	MedicineOfUser object (3)	1	[{"added": {}}]	6	1
7	2019-03-03 00:22:56.437951+00	4	MedicineOfUser object (4)	1	[{"added": {}}]	6	1
8	2019-03-03 06:45:37.316343+00	5	MedicineOfUser object (5)	1	[{"added": {}}]	6	1
9	2019-03-03 06:47:02.671587+00	6	MedicineOfUser object (6)	1	[{"added": {}}]	6	1
10	2019-03-03 08:06:46.663048+00	3	MedicineOfUser object (3)	2	[{"changed": {"fields": ["isAcceptedByPharmacist"]}}]	6	1
11	2019-03-03 08:07:15.859728+00	5	MedicineOfUser object (5)	2	[{"changed": {"fields": ["isRequested"]}}]	6	1
12	2019-03-03 08:48:06.123038+00	6	MedicineOfUser object (6)	2	[{"changed": {"fields": ["isRequested"]}}]	6	1
13	2019-03-03 08:48:20.831451+00	6	MedicineOfUser object (6)	2	[{"changed": {"fields": ["isRequested"]}}]	6	1
14	2019-03-03 08:48:28.078558+00	5	MedicineOfUser object (5)	2	[{"changed": {"fields": ["isRequested"]}}]	6	1
15	2019-03-03 09:28:59.218032+00	5	MedicineOfUser object (5)	2	[{"changed": {"fields": ["medicine"]}}]	6	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 15, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	group
3	auth	permission
4	contenttypes	contenttype
5	sessions	session
6	medex	medicineofuser
7	medex	medicine
8	useraccounts	usermodel
9	useraccounts	organisation
10	useraccounts	pharamcy
11	knox	authtoken
12	medex	requestedmedicines
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 12, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-03-02 09:00:29.386825+00
2	contenttypes	0002_remove_content_type_name	2019-03-02 09:00:29.399308+00
3	auth	0001_initial	2019-03-02 09:00:29.453912+00
4	auth	0002_alter_permission_name_max_length	2019-03-02 09:00:29.462525+00
5	auth	0003_alter_user_email_max_length	2019-03-02 09:00:29.472486+00
6	auth	0004_alter_user_username_opts	2019-03-02 09:00:29.480578+00
7	auth	0005_alter_user_last_login_null	2019-03-02 09:00:29.489726+00
8	auth	0006_require_contenttypes_0002	2019-03-02 09:00:29.492647+00
9	auth	0007_alter_validators_add_error_messages	2019-03-02 09:00:29.501507+00
10	auth	0008_alter_user_username_max_length	2019-03-02 09:00:29.509807+00
11	auth	0009_alter_user_last_name_max_length	2019-03-02 09:00:29.518451+00
12	useraccounts	0001_initial	2019-03-02 09:00:29.605237+00
13	admin	0001_initial	2019-03-02 09:00:29.636129+00
14	admin	0002_logentry_remove_auto_add	2019-03-02 09:00:29.650705+00
15	admin	0003_logentry_add_action_flag_choices	2019-03-02 09:00:29.668116+00
16	knox	0001_initial	2019-03-02 09:00:29.694716+00
17	knox	0002_auto_20150916_1425	2019-03-02 09:00:29.725369+00
18	knox	0003_auto_20150916_1526	2019-03-02 09:00:29.759204+00
19	knox	0004_authtoken_expires	2019-03-02 09:00:29.775237+00
20	knox	0005_authtoken_token_key	2019-03-02 09:00:29.795656+00
21	knox	0006_auto_20160818_0932	2019-03-02 09:00:29.85135+00
22	medex	0001_initial	2019-03-02 09:00:29.878116+00
23	medex	0002_auto_20190302_1149	2019-03-02 09:00:29.92406+00
24	medex	0003_auto_20190302_1423	2019-03-02 09:00:29.944895+00
25	sessions	0001_initial	2019-03-02 09:00:29.959272+00
26	medex	0004_auto_20190303_0638	2019-03-03 02:47:34.131985+00
27	medex	0005_auto_20190303_0705	2019-03-03 02:47:34.138504+00
28	medex	0006_auto_20190303_0736	2019-03-03 02:47:34.143963+00
29	useraccounts	0002_auto_20190303_0638	2019-03-03 02:47:34.181291+00
30	useraccounts	0003_auto_20190303_0723	2019-03-03 02:47:34.312792+00
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 30, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
8e6yzrb34rzigw4zr005v0bv3bvpo078	ZjgwYWRiNzE5N2ZjNzAwNGU3NDYyNGFiM2U1ZjhlYjA1ZjgzNzM1Yzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiJjYTUyNWVmYmI2NWVlZmM2M2FjZmU4ZWQ4OGE1ZDA1ODNjNzA5NTMwIn0=	2019-03-16 10:39:37.888233+00
\.


--
-- Data for Name: knox_authtoken; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.knox_authtoken (digest, salt, created, user_id, expires, token_key) FROM stdin;
72b924d81c853bde50045cfd31ffcfc001923be1536889cfbe49b101075e008b4e7007b3e21d2c1c7986a22b68e36f9d45bcf4ce71232651779452bc93cb2607	21a4d1d6b27f6934	2019-03-02 15:06:26.192826+00	2	2019-03-03 01:06:26.192344+00	de236767
9715aa55536a349d0798fe05bd73f53bfcc191e919fecae7f6f099ec7d45ee61ec6ddd705e26751b6d85322fed0e443dee60037a6a2dc98fb561864ceb16d0d2	e5307b7053c88ef7	2019-03-02 15:08:04.447685+00	2	2019-03-03 01:08:04.447034+00	fa0f6fbb
b917a0e16e7470089e4145c285d2b30ed787ce502ef603bd1119838cfce7496d01b5e223cb48defd3f5317700d18a53eae7b8c875a7a5611caf169f70bedcf4b	056fe9c7dc4ab50c	2019-03-02 15:09:50.244804+00	2	2019-03-03 01:09:50.244182+00	3531aab7
41451a28d704246b07174405719f01397385f8b61d46f18fd3657bfd5e1051089279b6d73ff391e79b03354aef2e977ccbb2560f0c4ed5df305be9a9f5c7a0af	f244451fd0d47723	2019-03-02 15:26:32.028866+00	2	2019-03-03 01:26:32.028338+00	ed5f4840
7a845b3831926da3772292a75351fac9111ecadb60f03d8b53c6d81654b689fa869da9f3a71598394489badf9a24f6bf805d8f4cb6efef19bb7a2e62940988b6	ee34780906fd02f4	2019-03-02 16:54:40.897477+00	5	2019-03-03 02:54:40.897065+00	df2bca51
03ea4a6b8dd2a7c14200e6b093252afd6f7d65d3f4a4358f28926c3cde2c207f6200b10006d834d1fc36dc2c58e34585a12cd943715fad70acc41bea5c2700a2	f47930a5b0786eda	2019-03-02 16:55:48.194624+00	6	2019-03-03 02:55:48.194126+00	534a438e
d631e58b150787c8c17693e5ce1d2d2111a6ce2161d9cec6145823ade4312d6cdb870c2655883fedfe766adafb2384a643ec4a01ed5bcb7b63430fb705d7e54e	3f8d3fd456912e71	2019-03-02 16:58:40.330265+00	7	2019-03-03 02:58:40.329958+00	ebdc7b26
e3073767d5e68b15e6f6dbad9dd7183f3e8caf0d23eb98d35b7c31f8b93b077d8d7c5eef9ce02253a9f280e8b983a40a728c57644315958ae3504e90abc69467	cc7f606eb3320dd6	2019-03-02 17:04:01.054722+00	9	2019-03-03 03:04:01.054172+00	8ec28b66
b6dd5949c9485d4790d65f9809763fd0a0f1eec8d200fc2f56d439bae63118773f9cf33b00dba56d85aa82702533518b9f837e2cfe599bea78c2db340f26fabc	6af0ea3505cc5a6d	2019-03-02 17:05:20.144577+00	10	2019-03-03 03:05:20.144128+00	85d5e0a6
2f224bde4e01e48c92382e0daa4148733be4d40cb7b3eb846fc5c55ceccbb518a47148d9bf84334e6b87580d2552722e5cb97bb34f18c014af34d49e2c4947b6	2e64a2a0ab13d2f7	2019-03-02 17:06:45.512641+00	11	2019-03-03 03:06:45.512344+00	8fcf5c0e
596cb030690afdd82ba742b1e4ad0305f5790fc62e4654ac7c52e5c5f8d9463bdb8f50ec3c6f129866fbd70739cff5b11b9ea719d44d44285ccdc25c72ba70a1	61c2ad0f2fc4a8cd	2019-03-02 22:58:25.689373+00	4	2019-03-03 08:58:25.689043+00	96a659d8
4e66c7fe820c224173a0cfc73217bed2bc7c76047e56ebe28b0dc678ab05528d7cc5f5404fe6b199558d52b835ce3c582493222e1b0a6b30e69294668e5bda84	0d655e64763213e1	2019-03-03 01:50:23.311951+00	3	2019-03-03 11:50:23.311424+00	bb32cdc5
8e111739c80b31c5e96ea8acddab611ac5c236578cb2421f97253ecb88f56240acdc986266abede4b49bd8682d9463ff71cdf1d33ee27cd8ba17249aceb78c5b	25826f82af149692	2019-03-03 03:21:16.350703+00	4	2019-03-03 13:21:16.350039+00	abf4674c
7d41487e4801757a47ef2a9f6a4fb78231d777403a8c9c8002f678acb5d4cdf6653e459f47cca62a342fd09431478531f8a1262c7ee34db912afe15a89e068a9	ad10864664bcf5ab	2019-03-03 03:25:43.262184+00	3	2019-03-03 13:25:43.261782+00	506d8c96
78a66ec3cea899883385af1d1a2a0b9cca2999efae35de710a2b9abd8537b3be4b173f8a0b409b6615f11a6fb8fe725970f3db8f34b76cd01b2cc39df06edfdb	148dd4046c92b40f	2019-03-03 03:27:01.791324+00	3	2019-03-03 13:27:01.790864+00	af0def89
3311596f274b1ff9e439398e93326dbc7bcdb6b6f7973de9b91ccb2881485414bc4891f67aae0911fefcd319a3285399648c8e3be2d857e04287d60cb1423e11	328dee54a087e0bb	2019-03-03 03:30:46.939848+00	4	2019-03-03 13:30:46.939469+00	91b64d0e
3c1dbcda7b94d333525c74602cd767a4d5ddefdc025ea453d530a6de4aa287b3425ff5c2b23a3002ccd5c424ed516936189853696ab897bcd8ce6a95f5cc42af	26165778b3219136	2019-03-03 04:35:16.73662+00	4	2019-03-03 14:35:16.736165+00	3c578a54
ba46e13a04f8b9e57e9dbe7ac7209c5e4fa64e1b69568d9ff2ff10e830abb86e1de78769a9f50a98f487bc094e6aa1b91a7f3e12515f27eb2a3de7d7db325d40	2daaebf2a97af11c	2019-03-03 04:42:06.957118+00	4	2019-03-03 14:42:06.956726+00	a2f3948e
e5f27c9538e84ab3c174155428ea0df2244fcd9f7cc747b224e91097c045969b720d31e65baa79c2b589a143b5ddf5ccebde12fda39fdee481a8287a4b1d13dd	fa9d0030dc05d77f	2019-03-03 05:10:04.945072+00	4	2019-03-03 15:10:04.944574+00	97515e9a
3ec0c4c92f24874f918d40e6ff8583b9b286a3e9e36023a74f29a32b9f346be0f35960c8a6aec5ebcb7036797d42ea6dbe25724541f6f746e65d8e70247ecccf	d31bdd52c068bf98	2019-03-03 06:09:24.728972+00	12	2019-03-03 16:09:24.72858+00	93835c13
f580d9f16a921eb4ac1318c818fcc0be38c3b2fda82a0b10d445cf84292995f5c9ad0540ff7887ca4dbf3b5b59756ca9ba3dcbbdfb4c430429ef4f4115780c7f	0b05e80b17c72611	2019-03-03 06:39:47.615999+00	4	2019-03-03 16:39:47.615563+00	f52add37
2117e7092ac69436621ab26d275f38c540ef13158e8deae75f362961d9f921720f5f81f351fedb12dcea776e34f363ce1d36445630eaf131dce09f014c86d08e	b0ce54e5633d99d4	2019-03-03 06:49:32.412966+00	8	2019-03-03 16:49:32.412434+00	eb255cf0
142be17aac1b877c15281af62d7043200dbffda889a722acd4abdad0bfbc9d212ba930a5c426f17733f8629a17adaf10b5be8236a795197c1c902c41f27d1851	73fa0364f0908965	2019-03-03 08:15:33.541881+00	4	2019-03-03 18:15:33.54156+00	62ea5194
a318aa6ff6d797fec6fb14533c985249881de71070edc499372e7b46a92a096f14dcf1e48eda40d0479e4eafc18203de15cbbd0e98b9f74fb50e2a7de4664736	2e9c3f609fc0b2d1	2019-03-03 08:26:33.996441+00	8	2019-03-03 18:26:33.995973+00	7af4041f
263c641b420f530be30d98cdb50d8715e4e07eb3ada14dc702c43d0a277273512557c8d856f4450a276474cd7ad148b5ae103c71c40f88ec636dea3cd77c71ec	14907fbea0ed8576	2019-03-03 08:28:07.286161+00	8	2019-03-03 18:28:07.285758+00	c975979b
9eb6610fef239a8c0c33497de2bdb97adbe994640bd39358466f8a67288e160dac9800690c7fbd017df6d9342f9475f2df72d71bcf38f84c273daa92a67477ab	20033020e347e4e8	2019-03-03 08:33:34.358692+00	8	2019-03-03 18:33:34.358287+00	fb33f93d
bfc283456751d9709c399e22085e0d7b46096ca7b7329f4d12b013ab13d12607c6be7058543d430354681b890254899ac8bfdc069ea06557c3609a18abfc254d	b2a76921199b342a	2019-03-03 08:35:16.213487+00	3	2019-03-03 18:35:16.213074+00	22adccd5
70e97eff2aa2ee6b505db8ed07a0798db524f581ef7e32cfb4589196bf545fc192ad6742b5b83f2a3aa092c26c2753de7c22386ba2c3121fae6e7edeefd4c86a	5b64a9f063845520	2019-03-03 08:48:27.776295+00	3	2019-03-03 18:48:27.775692+00	47907415
fc15c766ac1944aa16408cc67d3557adef1684098ff92de8f26ca4854522869596f82705916f9fa50ed4f68f329fa52968879da1dd1ad2cbb6f5a9d2f83c4d3e	b60e69ff06c9c14e	2019-03-03 08:51:53.736935+00	3	2019-03-03 18:51:53.736471+00	d91b5aa2
c76ddb18114de219e6a822929d7bbf8be27b6bc222d0af5eb3901b08614311d210eb1ff7d757e5e3b83800467c60b97111c94973125eca27723590127c30a716	fecf38c1efdddf31	2019-03-03 08:56:55.301801+00	3	2019-03-03 18:56:55.301244+00	d710b10b
acf4e844727461d512077b8ac64bf85b61c87faf787f6170d5f54cdfb09484494d0f394c5ae6d2de0e4785632e414f7390a6acb41d83d0114b73574135f32dbe	3b2791fbb82b6fda	2019-03-03 09:19:31.489705+00	8	2019-03-03 19:19:31.489399+00	68fc1e02
cf7853db26e521b47d0fd59ce4403f41264d1612007d24f1c0b31f9e7f77cb70c982ad7f8b0a0c587bde6c30a21f40cccb01df7c3d105fd3a721647430b35a4f	fd000d1d0a926dcc	2019-03-03 09:33:49.220488+00	8	2019-03-03 19:33:49.22013+00	5485b018
2637fadf2bf44b6bdc974b2fdff1ea5a7566846232f1ab6d56550867ce7115dab7174fd432c1cce7fb9d42db52d5ddce42618cbc405cb45fa6061792b6808965	35170c60ac4e4fc4	2019-03-03 09:43:18.902948+00	8	2019-03-03 19:43:18.902562+00	be805ef6
7cb93998ac75d732c5b0af9104eb14700984581a19f3f567ef902cd9e3aedc6de9f25d222e4170ffef8aad1896f012aa5add5d23fbcd54cfa86572e0ae3c6596	53d9316346ab06d5	2019-03-03 09:51:15.325589+00	8	2019-03-03 19:51:15.325104+00	672ecf94
a9d9576311a2a9f1537408e3d2b9c7b40ab973644b1fef421c24ad9a6ad7e3cfc448845ab876140aa62c911d462c32b01268035272cba9b3caec007b382195c5	82cdc0b151d2c27d	2019-03-03 10:04:12.344931+00	8	2019-03-03 20:04:12.344623+00	e7876d16
21291b4dac1b7670c532a4b4c1917f38fa3a5f37b55f6ecf3535f2de20eeb1b6f4214f670722908452f5e91d38527fafa2b1aeb2ea55a033c9689838d966ecb3	24a6fa15d82fcead	2019-03-03 10:12:47.781929+00	8	2019-03-03 20:12:47.781537+00	3c9cb775
ce4e8804fea74433e57293d9caee23b6e39a91a2bf1dafd986b0a46382d842dd39c68f3a0fd50c8552d30f61d50f47046c8600ba96260a590216cc92f3b18e64	c4e37aef34eab207	2019-03-03 10:13:37.707657+00	8	2019-03-03 20:13:37.707331+00	b585d37a
8a16f688dc0e0c74beadcb3f1f61b0ac9f664506b3d11712a0f72832156998877301bece0c8f4c546ce700b3759c0bdb3d1f3ff2f2e5ba1173c8e5c2b7e81c31	424b55941395cf8c	2019-03-03 10:21:28.084255+00	8	2019-03-03 20:21:28.083913+00	6e44d348
af3ce8fccf11c4b57f723b360609b4b019b8c76614353b2dccfa5de70516a7b88bb496d1a761501c8e2d7212dbd2a69a508d2168938faff07f3458f94d72ab02	b766f7437988383d	2019-03-03 10:22:03.924056+00	8	2019-03-03 20:22:03.923693+00	14dc4654
fd6f35215c335099658aac8f0097657e827eb3af77712b1afacbe2f4bbae5e84d13fb6c123c7e131b6d1e229e98dfeab713022ad544a659907f225e5d5331824	21c11f3606072f6b	2019-03-03 10:42:19.017442+00	8	2019-03-03 20:42:19.016436+00	26d15e37
c6f0973c1bd5dcff588cd7452a6e0fec39060d7be36bcc3e1b3c810a97efdec54670a44609fdb781b0c4a36a60e9951719fd3fd4bc0b79f98bbc0a403eea67de	f26e5416adc6f597	2019-03-03 10:43:12.934038+00	8	2019-03-03 20:43:12.933668+00	e575cf0e
9fb8634f44c8dc88876feb496950557f6c7bddf256a3d5e84a9522ed9559282a67015cfe4ba96873873c8907cd320718b91201149b0b2026f79ea1df1b110228	d06b258458413abd	2019-03-03 10:53:45.278779+00	8	2019-03-03 20:53:45.278288+00	38935092
72d892eccf4f20c314bacaf7d35bf78d7c51a3b65d30d932da91057580d44a321819ca8d4ef44fd90b745e30ad7bedc8d6a25358835705786f84a8a2fd036865	e051d8289f216b8c	2019-03-03 10:54:28.516207+00	8	2019-03-03 20:54:28.514319+00	cfbb6dda
22db9299eefc4247293bab7898dbb34f33dc52d85407cea0365cdc753ef5b3ffba78a96b6753fc2d0e5f74bddf5dc9e136d44c944b6d07bc79f74d134c64349c	7d65b70ad0cc88da	2019-03-06 08:51:49.312925+00	15	2019-03-06 18:51:49.31243+00	96287353
3a26e6d5ba3d5db4d682b9f2c22150fb5851914b1a7ceb8cd1967644057f52fd1bf6ad664da23d47bf5145c41d2839bb9361d5f51b8312e88186654e4284dd09	5d0ffda451f099f4	2019-03-07 14:35:05.052512+00	16	2019-03-08 00:35:05.051794+00	95796201
\.


--
-- Data for Name: medex_medicine; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.medex_medicine (id, created_at, updated_at, name, mrp, quantity, "pricePerTablet") FROM stdin;
1	2019-03-02 17:59:36.698702+00	2019-03-02 17:59:36.69876+00	Calpol 650	31.50	15	2.1000000000
2	2019-03-02 18:14:39.050275+00	2019-03-02 18:14:39.050322+00	stemetil	71.00	10	7.1000000000
3	2019-03-02 18:15:26.840108+00	2019-03-02 18:15:26.840161+00	Cyara-D	43.00	10	4.3000000000
4	2019-03-02 18:17:24.04591+00	2019-03-02 18:17:24.045949+00	Norflox	73.00	10	7.3000000000
5	2019-03-02 18:17:50.824979+00	2019-03-02 18:17:50.825049+00	metrogyl	54.00	10	5.4000000000
6	2019-03-02 18:22:42.876092+00	2019-03-02 18:22:42.876161+00	ondem	50.00	10	5.0000000000
7	2019-03-02 18:26:55.628413+00	2019-03-02 18:26:55.628453+00	digene	12.00	9	1.3333333333
8	2019-03-02 18:29:43.190523+00	2019-03-02 18:29:43.190571+00	Etizolam	31.00	10	3.1000000000
9	2019-03-02 18:30:14.820029+00	2019-03-02 18:30:14.820084+00	Mobizox	150.00	10	15.0000000000
10	2019-03-02 18:31:15.467535+00	2019-03-02 18:31:15.467638+00	Telmaxx	172.00	10	17.2000000000
11	2019-03-02 18:32:55.065844+00	2019-03-02 18:32:55.065879+00	Flagyl 400mg	12.00	15	0.8000000000
12	2019-03-02 18:33:28.446873+00	2019-03-02 18:33:28.44691+00	Ocid 20mg	39.00	10	3.9000000000
13	2019-03-02 18:34:36.568169+00	2019-03-02 18:34:36.568207+00	Atarax 10mg	30.00	15	2.0000000000
14	2019-03-02 18:35:32.54719+00	2019-03-02 18:35:32.54724+00	Cetzine	16.00	10	1.6000000000
15	2019-03-02 18:36:22.482207+00	2019-03-02 18:36:22.482242+00	Cifran CTH	60.00	10	6.0000000000
16	2019-03-02 18:37:02.127131+00	2019-03-02 18:37:02.12717+00	Veloz-20mg	117.00	15	7.8000000000
17	2019-03-02 18:38:06.875753+00	2019-03-02 18:38:06.875792+00	Zinase DP	122.00	10	12.2000000000
18	2019-03-02 18:39:21.784993+00	2019-03-02 18:39:21.785028+00	Vibact DS	160.00	10	16.0000000000
19	2019-03-03 01:24:06.190991+00	2019-03-03 01:24:06.191037+00	Ecpan DSR	116.00	10	11.6000000000
20	2019-03-03 01:29:04.265927+00	2019-03-03 01:29:04.265959+00	Bipra 20mg	75.00	10	7.5000000000
21	2019-03-03 01:29:51.454507+00	2019-03-03 01:29:51.454542+00	Dompan SR	117.00	10	11.7000000000
22	2019-03-03 01:31:05.667146+00	2019-03-03 01:31:05.667196+00	Drego D	89.00	10	8.9000000000
23	2019-03-03 01:32:07.1752+00	2019-03-03 01:32:07.175238+00	Ezorb D3	225.00	10	22.5000000000
24	2019-03-03 01:33:22.881486+00	2019-03-03 01:33:22.881534+00	Dyoflux	120.00	10	12.0000000000
25	2019-03-03 01:34:19.324971+00	2019-03-03 01:34:19.325007+00	Esoford 40mg	65.00	10	6.5000000000
26	2019-03-03 01:35:40.795488+00	2019-03-03 01:35:40.795525+00	Beminal total	203.00	10	20.3000000000
27	2019-03-03 01:37:30.07965+00	2019-03-03 01:37:30.079687+00	D-Kool	82.00	10	8.2000000000
28	2019-03-03 01:38:31.333797+00	2019-03-03 01:38:31.333845+00	Caleat TH	178.00	10	17.8000000000
29	2019-03-03 02:43:16.965036+00	2019-03-03 02:43:16.965074+00	Calcijoint XT	95.00	15	6.3333333333
30	2019-03-03 03:37:38.983181+00	2019-03-03 03:37:38.983219+00	Ecrab 20mg	58.00	10	5.8000000000
31	2019-03-03 03:39:24.007498+00	2019-03-03 03:39:24.007537+00	Blendomol	95.00	10	9.5000000000
32	2019-03-03 04:05:34.569492+00	2019-03-03 04:05:34.569555+00	Bowcid 20mg	45.00	10	4.5000000000
33	2019-03-03 05:30:49.914617+00	2019-03-03 05:30:49.914656+00	Ventrab  20mg	60.00	10	6.0000000000
34	2019-03-03 05:35:51.205178+00	2019-03-03 05:35:51.205213+00	Victorab DSR	70.00	10	7.0000000000
35	2019-03-03 05:37:58.247587+00	2019-03-03 05:37:58.247626+00	Veocal	86.00	15	5.7333333333
36	2019-03-03 05:43:46.465385+00	2019-03-03 05:43:46.465435+00	Weltop DM	59.00	10	5.9000000000
37	2019-03-03 05:46:09.764327+00	2019-03-03 05:46:09.764367+00	Zorip DSR	97.00	10	9.7000000000
\.


--
-- Name: medex_medicine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.medex_medicine_id_seq', 37, true);


--
-- Data for Name: medex_medicineofuser; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.medex_medicineofuser (id, created_at, updated_at, "creditForMedicine", "expiryDate", "medicinePicture", "expiryPicture", "quantityOfMedicine", "isSoldByPharmacist", "isAcceptedByPharmacist", "isRequested", medicine_id, pharmacist_id, user_id) FROM stdin;
2	2019-03-03 00:20:15.77284+00	2019-03-03 00:17:17.093159+00	13.65	2019-05-03	medicine/user_2/medicine_12/ss.png	expirydate/user_2/medicine_12/ss.png	7	f	t	f	12	7	2
1	2019-03-03 00:20:22.156123+00	2019-03-03 00:16:20.719115+00	18.25	2019-06-01	medicine/user_2/medicine_4/ss.png	expirydate/user_2/medicine_4/ss.png	5	f	t	f	4	4	2
4	2019-03-03 00:22:56.435919+00	2019-03-03 00:22:56.435948+00	42.70	2019-10-05	medicine/user_2/medicine_17/ss.png	expirydate/user_2/medicine_17/ss.png	7	f	t	f	17	11	2
3	2019-03-03 08:06:46.660894+00	2019-03-03 00:21:58.23976+00	9.45	2019-11-30	medicine/user_3/medicine_1/ss.png	expirydate/user_3/medicine_1/ss.png	9	f	f	f	1	9	3
6	2019-03-03 08:48:20.827945+00	2019-03-03 06:47:02.659645+00	60.20	2019-08-30	medicine/user_2/medicine_10/ss.png	expirydate/user_2/medicine_10/ss.png	7	f	f	t	10	8	2
5	2019-03-03 09:28:59.215763+00	2019-03-03 06:45:37.310261+00	8.40	2019-07-02	medicine/user_3/medicine_1/ss_PKRvvEH.png	expirydate/user_3/medicine_1/ss_ZDjRewr.png	8	f	f	t	4	5	3
7	2019-03-03 09:51:38.078549+00	2019-03-03 09:51:38.078584+00	8.00	2019-03-23			12	f	f	f	7	\N	3
8	2019-03-03 09:54:45.20875+00	2019-03-03 09:54:45.208798+00	8.00	2019-03-15			12	f	f	f	7	\N	3
9	2019-03-03 11:33:23.6593+00	2019-03-03 11:32:19.393608+00	213.60	2019-03-23			12	f	f	t	28	9	3
\.


--
-- Name: medex_medicineofuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.medex_medicineofuser_id_seq', 9, true);


--
-- Data for Name: medex_requestedmedicines; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.medex_requestedmedicines (id, created_at, updated_at, "medicineRequested", details, "isAccepted") FROM stdin;
\.


--
-- Name: medex_requestedmedicines_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.medex_requestedmedicines_id_seq', 1, false);


--
-- Data for Name: useraccounts_organisation; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.useraccounts_organisation (usermodel_ptr_id, latitude, longitude, "licenseOfOrganisation", "licenseNumber") FROM stdin;
\.


--
-- Data for Name: useraccounts_pharamcy; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.useraccounts_pharamcy (usermodel_ptr_id, latitude, longitude, "licenseOfPharmacist", "licenseNumber") FROM stdin;
4	13.055306	77.602988	pharmacistlicense/PharmaDoc.pdf	0
5	13.076853	77.663900	pharmacistlicense/PharmaDoc_nlR9Ur8.pdf	0
6	12.9589248	77.60527359999999	pharmacistlicense/PharmaDoc_vjbjm04.pdf	0
7	13.038420	77.617420	pharmacistlicense/PharmaDoc_ITNaXId.pdf	0
8	13.038420	77.617420	pharmacistlicense/PharmaDoc_xKfb8Pj.pdf	0
9	13.064979	77.631672	pharmacistlicense/PharmaDoc_2rgWmL9.pdf	0
10	13.055210	77.599370	pharmacistlicense/PharmaDoc_kZDrkNr.pdf	0
11	13.026130	77.634750	pharmacistlicense/PharmaDoc_EDAnBD8.pdf	0
12	12.9589248	77.663900		1113344
\.


--
-- Data for Name: useraccounts_usermodel; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.useraccounts_usermodel (id, password, last_login, is_superuser, first_name, last_name, is_staff, is_active, date_joined, username, email, "aadhaarNo", address, "zipCode", "totalCredits", "phoneNumber") FROM stdin;
1	pbkdf2_sha256$120000$enCmc83ViURf$t8fZgqib0E/qpsri8UG0b5G/kA6rK3L1PJmcZ9LUxgk=	2019-03-02 10:39:37.885399+00	t			t	t	2019-03-02 09:02:34.738124+00	Divag	divag.bvp@gmail.com	111122223333			0.00	
4	pbkdf2_sha256$120000$bepAgwoy2sGE$V5pQTUk0GcWu2hAvzyyPR+Quby/umZisTBu7Uw8ClF0=	\N	f			f	t	2019-03-02 16:53:05.634046+00	Sandeep Medicals	pharma1@gmail.com	123423454567	Dasarahalli Main Rd, Bhuvaneswari Nagar, Hebbal Kempapura, Bengaluru, Karnataka 560024		0.00	9899812345
5	pbkdf2_sha256$120000$qEwDC17gVrhG$7QopnCFEEgnf0CX5YY363LXBeMT790znOrAr5FOrm1s=	\N	f			f	t	2019-03-02 16:54:40.732182+00	RVM Philanthopic Home	pharma2@gmail.com	123423454567	1, Chikkagubbi Main Rd, Chikkagubbi Village, Chikkagubbi, Karnataka 560077		0.00	9899812345
6	pbkdf2_sha256$120000$bNqMWSgqHHyr$ragePcC514dcDC6PFDwntO9TdIbWQUhaoAhT5czRpNE=	\N	f			f	t	2019-03-02 16:55:48.058849+00	MedPlus	pharma3@gmail.com	123423454567	13th Main Road Vinayaka Layout, Hebbal Kempapura, Byatarayanapura CMC and OG Part, Bengaluru, Karnataka 560024		0.00	9899812345
7	pbkdf2_sha256$120000$an7M0j7UhrOi$uDJdHhpsYD8OxmY/bkPgfGXhGJdg3Q5sLpdsz27MXFA=	\N	f			f	t	2019-03-02 16:58:40.189746+00	Maruti Medicals	pharma4@gmail.com	123423454567	5th Block, Vyalikaval HBCS Layout, Nagavara, Bengaluru, Karnataka 560045		0.00	9899812345
8	pbkdf2_sha256$120000$cAxAcRAgznhM$vrLMXmYevr03PG9xoloMFI+q/jnxzLzqrvzsD8jasaA=	\N	f			f	t	2019-03-02 17:02:34.80058+00	Apollo Pharmacy	pharma5@gmail.com	123423454567	No 5, Sultanpalya Main Rd, Hullurappa Layout, Bhuvaneswari Nagar, Hebbal, Bengaluru, Karnataka 560032		0.00	9899812345
9	pbkdf2_sha256$120000$L9jsWpEVnUEC$zV8DLH3oVItRcrtfoxFtHDg/4+7w7DCBu4rrg8OpCpU=	\N	f			f	t	2019-03-02 17:04:00.895661+00	United Pharma	pharma6@gmail.com	123423454567	Ashwath Nagar, Sinthan, 300, Thanisandra Main Rd, Sampangi Rama Nagar, Ashwath Nagar, Bengaluru, Karnataka 560045		0.00	9899812345
10	pbkdf2_sha256$120000$gZLDt0oGhZ3F$6ufp0om0pbiM586/2Dya4HIX7tZRRf3WAhotUhm1rCk=	\N	f			f	t	2019-03-02 17:05:20.002809+00	Pulse Pharmacy	pharma7@gmail.com	123423454567	Dasarahalli Main Rd, Hebbal Kempapura, Bengaluru, Karnataka 560024		0.00	9899812345
11	pbkdf2_sha256$120000$XzpRtY9eKjd8$pXunyncRx6id43RUutZQ2Ms6fjw/IbKhyvnCul7I8FM=	\N	f			f	t	2019-03-02 17:06:45.372995+00	Ram Medicals	pharma8@gmail.com	123423454567	139/68, 1st A Cross Rd, 5th Block, Telecom Layout, HBR Layout, Bengaluru, Karnataka 560043		0.00	9899812345
3	pbkdf2_sha256$120000$urKQxnhmaEKI$30FlQh8rsEhaSL5FUI82fKQNNSnv+R7ZmKeewkDG7WM=	\N	f			f	t	2019-03-02 15:28:29.093216+00	DivBVCOE	divag.bvcoe@gmail.com	123456789012	Address 142		18.90	1234567890
2	pbkdf2_sha256$120000$jcwxyIc7lBN3$qzvXeg2DGL9K1QAhN5kH+9dxLh9fs/g8DzK288vj+lI=	\N	f			f	t	2019-03-02 15:06:26.039949+00	kunalraghav	kunalraghav@rocketmail.com	123456789012	address 12		149.20	9810390605
12	pbkdf2_sha256$120000$gcIEVuoWuUQm$9irSniu19q+dpa4Q9/FwK2ClCBSFJ4uHWvrgPwmZjiA=	\N	f			f	t	2019-03-03 06:09:24.572247+00	MedPlus	pharma11@gmail.com	111122223333	13th Main Road Vinayaka Layout, Hebbal Kempapura, Byatarayanapura CMC and OG Part,\nBengaluru, Karnataka 560024		0.00	1234567890
13	pbkdf2_sha256$120000$xNry7LX3k9Zf$Z4ihi1H3qlJSH0/QwJh3wqUSL5rVGswoWRn+AasTE4c=	\N	f			f	t	2019-03-03 09:18:41.657032+00	Vansh Kapoor	vanshkapoorvk7@gmail.com	342342	NP, 79A		0.00	9582347770
14	pbkdf2_sha256$120000$dULHkJM41fUz$Zeqhd7XKBEPrbYOFAg4NF3c8mW4kRvqrkvYFRubCh9g=	\N	f			f	t	2019-03-05 19:47:56.109735+00	vansh	vanshkapoors@gmail.com	121212	tp-53		0.00	9582347770
15	pbkdf2_sha256$120000$kWhPVxy9kUKy$jmRCKCTHoGzQcoElWUmXS4aHYx637QDzc7x9ihUGxT4=	\N	f			f	t	2019-03-06 08:51:49.159866+00	bhumika	bhumika@gmail.com	54546	g37		0.00	9716040900
16	pbkdf2_sha256$120000$onVYdJfcls9N$R6D2VtGDDUXJaCUw+FfEHf5xk/q9UDq1Oq9lPXT2A7Q=	\N	f			f	t	2019-03-07 14:35:04.798659+00	antriksh	antriksh@gmail.com	545454	tp-53		0.00	9898989898
\.


--
-- Data for Name: useraccounts_usermodel_groups; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.useraccounts_usermodel_groups (id, usermodel_id, group_id) FROM stdin;
\.


--
-- Name: useraccounts_usermodel_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.useraccounts_usermodel_groups_id_seq', 1, false);


--
-- Name: useraccounts_usermodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.useraccounts_usermodel_id_seq', 16, true);


--
-- Data for Name: useraccounts_usermodel_user_permissions; Type: TABLE DATA; Schema: public; Owner: azomicrate
--

COPY public.useraccounts_usermodel_user_permissions (id, usermodel_id, permission_id) FROM stdin;
\.


--
-- Name: useraccounts_usermodel_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: azomicrate
--

SELECT pg_catalog.setval('public.useraccounts_usermodel_user_permissions_id_seq', 1, false);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: knox_authtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.knox_authtoken
    ADD CONSTRAINT knox_authtoken_pkey PRIMARY KEY (digest);


--
-- Name: knox_authtoken_salt_key; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.knox_authtoken
    ADD CONSTRAINT knox_authtoken_salt_key UNIQUE (salt);


--
-- Name: medex_medicine_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.medex_medicine
    ADD CONSTRAINT medex_medicine_pkey PRIMARY KEY (id);


--
-- Name: medex_medicineofuser_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.medex_medicineofuser
    ADD CONSTRAINT medex_medicineofuser_pkey PRIMARY KEY (id);


--
-- Name: medex_requestedmedicines_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.medex_requestedmedicines
    ADD CONSTRAINT medex_requestedmedicines_pkey PRIMARY KEY (id);


--
-- Name: useraccounts_organisation_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_organisation
    ADD CONSTRAINT useraccounts_organisation_pkey PRIMARY KEY (usermodel_ptr_id);


--
-- Name: useraccounts_pharamcy_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_pharamcy
    ADD CONSTRAINT useraccounts_pharamcy_pkey PRIMARY KEY (usermodel_ptr_id);


--
-- Name: useraccounts_usermodel_email_key; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel
    ADD CONSTRAINT useraccounts_usermodel_email_key UNIQUE (email);


--
-- Name: useraccounts_usermodel_g_usermodel_id_group_id_df06a72a_uniq; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_groups
    ADD CONSTRAINT useraccounts_usermodel_g_usermodel_id_group_id_df06a72a_uniq UNIQUE (usermodel_id, group_id);


--
-- Name: useraccounts_usermodel_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_groups
    ADD CONSTRAINT useraccounts_usermodel_groups_pkey PRIMARY KEY (id);


--
-- Name: useraccounts_usermodel_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel
    ADD CONSTRAINT useraccounts_usermodel_pkey PRIMARY KEY (id);


--
-- Name: useraccounts_usermodel_u_usermodel_id_permission__6b3ca791_uniq; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_user_permissions
    ADD CONSTRAINT useraccounts_usermodel_u_usermodel_id_permission__6b3ca791_uniq UNIQUE (usermodel_id, permission_id);


--
-- Name: useraccounts_usermodel_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_user_permissions
    ADD CONSTRAINT useraccounts_usermodel_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: knox_authtoken_digest_188c7e77_like; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX knox_authtoken_digest_188c7e77_like ON public.knox_authtoken USING btree (digest varchar_pattern_ops);


--
-- Name: knox_authtoken_salt_3d9f48ac_like; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX knox_authtoken_salt_3d9f48ac_like ON public.knox_authtoken USING btree (salt varchar_pattern_ops);


--
-- Name: knox_authtoken_token_key_8f4f7d47; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX knox_authtoken_token_key_8f4f7d47 ON public.knox_authtoken USING btree (token_key);


--
-- Name: knox_authtoken_token_key_8f4f7d47_like; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX knox_authtoken_token_key_8f4f7d47_like ON public.knox_authtoken USING btree (token_key varchar_pattern_ops);


--
-- Name: knox_authtoken_user_id_e5a5d899; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX knox_authtoken_user_id_e5a5d899 ON public.knox_authtoken USING btree (user_id);


--
-- Name: medex_medicineofuser_medicine_id_38bbff8d; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX medex_medicineofuser_medicine_id_38bbff8d ON public.medex_medicineofuser USING btree (medicine_id);


--
-- Name: medex_medicineofuser_pharmacist_id_f988aa87; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX medex_medicineofuser_pharmacist_id_f988aa87 ON public.medex_medicineofuser USING btree (pharmacist_id);


--
-- Name: medex_medicineofuser_user_id_bea7a690; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX medex_medicineofuser_user_id_bea7a690 ON public.medex_medicineofuser USING btree (user_id);


--
-- Name: useraccounts_usermodel_email_e292601d_like; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX useraccounts_usermodel_email_e292601d_like ON public.useraccounts_usermodel USING btree (email varchar_pattern_ops);


--
-- Name: useraccounts_usermodel_groups_group_id_d412f63e; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX useraccounts_usermodel_groups_group_id_d412f63e ON public.useraccounts_usermodel_groups USING btree (group_id);


--
-- Name: useraccounts_usermodel_groups_usermodel_id_6584e1ac; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX useraccounts_usermodel_groups_usermodel_id_6584e1ac ON public.useraccounts_usermodel_groups USING btree (usermodel_id);


--
-- Name: useraccounts_usermodel_user_permissions_permission_id_0ed166a7; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX useraccounts_usermodel_user_permissions_permission_id_0ed166a7 ON public.useraccounts_usermodel_user_permissions USING btree (permission_id);


--
-- Name: useraccounts_usermodel_user_permissions_usermodel_id_1ef0fc93; Type: INDEX; Schema: public; Owner: azomicrate
--

CREATE INDEX useraccounts_usermodel_user_permissions_usermodel_id_1ef0fc93 ON public.useraccounts_usermodel_user_permissions USING btree (usermodel_id);


--
-- Name: auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_c564eba6_fk_useraccounts_usermodel_id; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_useraccounts_usermodel_id FOREIGN KEY (user_id) REFERENCES public.useraccounts_usermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: knox_authtoken_user_id_e5a5d899_fk_useraccounts_usermodel_id; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.knox_authtoken
    ADD CONSTRAINT knox_authtoken_user_id_e5a5d899_fk_useraccounts_usermodel_id FOREIGN KEY (user_id) REFERENCES public.useraccounts_usermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medex_medicineofuser_medicine_id_38bbff8d_fk_medex_medicine_id; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.medex_medicineofuser
    ADD CONSTRAINT medex_medicineofuser_medicine_id_38bbff8d_fk_medex_medicine_id FOREIGN KEY (medicine_id) REFERENCES public.medex_medicine(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medex_medicineofuser_pharmacist_id_f988aa87_fk_useraccou; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.medex_medicineofuser
    ADD CONSTRAINT medex_medicineofuser_pharmacist_id_f988aa87_fk_useraccou FOREIGN KEY (pharmacist_id) REFERENCES public.useraccounts_pharamcy(usermodel_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medex_medicineofuser_user_id_bea7a690_fk_useraccou; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.medex_medicineofuser
    ADD CONSTRAINT medex_medicineofuser_user_id_bea7a690_fk_useraccou FOREIGN KEY (user_id) REFERENCES public.useraccounts_usermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: useraccounts_organis_usermodel_ptr_id_1ceb89ee_fk_useraccou; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_organisation
    ADD CONSTRAINT useraccounts_organis_usermodel_ptr_id_1ceb89ee_fk_useraccou FOREIGN KEY (usermodel_ptr_id) REFERENCES public.useraccounts_usermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: useraccounts_pharamc_usermodel_ptr_id_23f09248_fk_useraccou; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_pharamcy
    ADD CONSTRAINT useraccounts_pharamc_usermodel_ptr_id_23f09248_fk_useraccou FOREIGN KEY (usermodel_ptr_id) REFERENCES public.useraccounts_usermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: useraccounts_usermod_group_id_d412f63e_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_groups
    ADD CONSTRAINT useraccounts_usermod_group_id_d412f63e_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: useraccounts_usermod_permission_id_0ed166a7_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_user_permissions
    ADD CONSTRAINT useraccounts_usermod_permission_id_0ed166a7_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: useraccounts_usermod_usermodel_id_1ef0fc93_fk_useraccou; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_user_permissions
    ADD CONSTRAINT useraccounts_usermod_usermodel_id_1ef0fc93_fk_useraccou FOREIGN KEY (usermodel_id) REFERENCES public.useraccounts_usermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: useraccounts_usermod_usermodel_id_6584e1ac_fk_useraccou; Type: FK CONSTRAINT; Schema: public; Owner: azomicrate
--

ALTER TABLE ONLY public.useraccounts_usermodel_groups
    ADD CONSTRAINT useraccounts_usermod_usermodel_id_6584e1ac_fk_useraccou FOREIGN KEY (usermodel_id) REFERENCES public.useraccounts_usermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

