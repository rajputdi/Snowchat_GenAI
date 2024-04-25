USE ROLE ACCOUNTADMIN;

-- Databases
CREATE OR REPLACE DATABASE HOL_DB;

-- Warehouses
CREATE OR REPLACE WAREHOUSE HOL_WH WAREHOUSE_SIZE = XSMALL, AUTO_SUSPEND = 300, AUTO_RESUME= TRUE;


-- Create the database level objects
USE WAREHOUSE HOL_WH;
USE DATABASE HOL_DB;

-- Schemas
CREATE OR REPLACE SCHEMA PUBLIC;
CREATE OR REPLACE SCHEMA RAW;
CREATE OR REPLACE SCHEMA ANALYTICS;