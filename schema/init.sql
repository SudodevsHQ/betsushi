create table if not exists users
(
    id         varchar primary key,
    full_name  varchar,
    currency   varchar,
    created_at timestamp default now()
);

create table if not exists account
(
    id         varchar primary key,
    balance    double precision,
    contact_id varchar,
    user_id    varchar,
    created_at timestamp default now(),
    constraint fk_account_users foreign key (user_id) references users (id)

);

create table if not exists upi
(
    id         varchar primary key,
    user_id    varchar,
    created_at timestamp default now(),
    constraint fk_upi_user foreign key (user_id) references users (id)
);

create type transaction_type as enum ('send', 'receive');
create type transaction_status as enum ('queued', 'pending', 'rejected', 'processing', 'processed', 'cancelled', 'reversed');

create table if not exists transaction
(
    id              serial primary key,
    razorpay_tid    varchar,
    amount          double precision,
    user_id         varchar,
    type            transaction_type,
    fund_account_id varchar null,
    upi             varchar,
    status          transaction_status,
    created_at      timestamp default now(),
    constraint fk_transaction_users foreign key (user_id) references users (id)

);