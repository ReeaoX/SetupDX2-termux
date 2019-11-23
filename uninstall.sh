#!/bin/#!/usr/bin/env bash

if [ -f "$DX2BAK/.bashrc" ]; then
  cp $DX2BAK/.bashrc ~/.bashrc;
elif [ -f "$DX2BAK/.bashrc.bak" ]; then
  cp $DX2BAK/.bashrc.bak ~/.bashrc;
fi

if [ -f "$DX2BAK/.zshrc" ]; then
  cp $DX2BAK/.zshrc ~/.zshrc;
elif [ -f "$DX2BAK/.zshrc.bak" ]; then
  cp $DX2BAK/.zshrc.bak ~/.zshrc;
fi

if [ -f "$HOME/.dx2rc" ]; then
  rm "$HOME/.dx2rc";
fi

rm -rf "$HOME/.DX2";
