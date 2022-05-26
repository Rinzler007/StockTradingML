def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9758
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 62, Entropy: 0.997
      if obj[0]>41.534:
         # Feature: RSI, Instances: 46, Entropy: 0.9656
         if obj[1] == 'Hold':
            # Feature: SMA1, Instances: 44, Entropy: 0.976
            if obj[4] == 'Buy':
               # Feature: SMA2, Instances: 28, Entropy: 0.9963
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 17, Entropy: 0.9774
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 11, Entropy: 0.994
                  if obj[2] == 'Sell':
                     return 'Yes'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'Yes'
            elif obj[4] == 'Sell':
               # Feature: MACD, Instances: 16, Entropy: 0.896
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 13, Entropy: 0.9612
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[1] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[0]<=41.534:
         # Feature: MACD, Instances: 16, Entropy: 0.896
         if obj[2] == 'Sell':
            # Feature: SMA1, Instances: 8, Entropy: 1.0
            if obj[4] == 'Buy':
               # Feature: SMA2, Instances: 5, Entropy: 0.971
               if obj[5] == 'Buy':
                  # Feature: RSI, Instances: 3, Entropy: 0.9183
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: RSI, Instances: 2, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: SMA2, Instances: 3, Entropy: 0.9183
               if obj[5] == 'Buy':
                  # Feature: RSI, Instances: 2, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[2] == 'Buy':
            # Feature: SMA1, Instances: 8, Entropy: 0.5436
            if obj[4] == 'Sell':
               return 'Yes'
            elif obj[4] == 'Buy':
               # Feature: SMA2, Instances: 2, Entropy: 1.0
               if obj[5] == 'Sell':
                  return 'No'
               elif obj[5] == 'Buy':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: Closing, Instances: 48, Entropy: 0.7383
      if obj[0]>41.534:
         # Feature: SMA1, Instances: 31, Entropy: 0.8691
         if obj[4] == 'Buy':
            # Feature: SMA2, Instances: 17, Entropy: 0.6723
            if obj[5] == 'Buy':
               # Feature: RSI, Instances: 16, Entropy: 0.5436
               if obj[1] == 'Sell':
                  return 'Yes'
               elif obj[1] == 'Hold':
                  # Feature: MACD, Instances: 8, Entropy: 0.8113
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               return 'No'
            else:
               return 'No'
         elif obj[4] == 'Sell':
            # Feature: SMA2, Instances: 14, Entropy: 0.9852
            if obj[5] == 'Buy':
               # Feature: RSI, Instances: 9, Entropy: 0.9911
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 6, Entropy: 1.0
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[1] == 'Sell':
                  # Feature: MACD, Instances: 3, Entropy: 0.9183
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Sell':
               # Feature: RSI, Instances: 5, Entropy: 0.7219
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 4, Entropy: 0.8113
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[1] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[0]<=41.534:
         # Feature: MACD, Instances: 17, Entropy: 0.3228
         if obj[2] == 'Buy':
            return 'Yes'
         elif obj[2] == 'Sell':
            return 'No'
         else:
            return 'No'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      # Feature: Closing, Instances: 5, Entropy: 0.7219
      if obj[0]<=41.534:
         # Feature: RSI, Instances: 3, Entropy: 0.9183
         if obj[1] == 'Hold':
            # Feature: MACD, Instances: 3, Entropy: 0.9183
            if obj[2] == 'Sell':
               # Feature: SMA1, Instances: 3, Entropy: 0.9183
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[0]>41.534:
         return 'No'
      else:
         return 'No'
   else:
      return 'No'
