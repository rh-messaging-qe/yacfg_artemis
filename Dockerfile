FROM quay.io/rhmessagingqe/yacfg:latest
COPY profiles /data/profiles
COPY templates /data/templates

ENV YACFG_TEMPLATES=/data/templates
ENV YACFG_PROFILES=/data/profiles
