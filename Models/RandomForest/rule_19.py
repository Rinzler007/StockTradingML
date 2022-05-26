def findDecision(obj):
   # Feature: RSI, Instances: 115, Entropy: 0.9986
   if obj[1] == 'Hold':
      # Feature: Closing, Instances: 97, Entropy: 0.9981
      if obj[0]>37.360001:
         # Feature: BB, Instances: 71, Entropy: 0.9676
         if obj[3] == 'Sell':
            # Feature: SMA2, Instances: 50, Entropy: 0.9044
            if obj[5] == 'Sell':
               # Feature: SMA1, Instances: 29, Entropy: 0.7355
               if obj[4] == 'Sell':
                  # Feature: MACD, Instances: 15, Entropy: 0.5665
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: MACD, Instances: 14, Entropy: 0.8631
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               # Feature: MACD, Instances: 21, Entropy: 0.9984
               if obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 18, Entropy: 1.0
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 3, Entropy: 0.9183
                  if obj[4] == 'Sell':
                     return 'No'
                  elif obj[4] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[3] == 'Hold':
            # Feature: SMA1, Instances: 19, Entropy: 0.9495
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 10, Entropy: 0.7219
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 6, Entropy: 0.65
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 4, Entropy: 0.8113
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[4] == 'Sell':
               # Feature: SMA2, Instances: 9, Entropy: 0.9911
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 5, Entropy: 0.7219
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: MACD, Instances: 4, Entropy: 0.8113
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[3] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[0]<=37.360001:
         # Feature: BB, Instances: 26, Entropy: 0.8905
         if obj[3] == 'Sell':
            # Feature: SMA1, Instances: 21, Entropy: 0.9587
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 13, Entropy: 0.9957
               if obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 9, Entropy: 0.9183
                  if obj[5] == 'Buy':
                     return 'Yes'
                  elif obj[5] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 4, Entropy: 0.8113
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: SMA2, Instances: 8, Entropy: 0.8113
               if obj[5] == 'Sell':
                  # Feature: MACD, Instances: 6, Entropy: 0.65
                  if obj[2] == 'Buy':
                     return 'Yes'
                  elif obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Buy':
                  # Feature: MACD, Instances: 2, Entropy: 1.0
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'No'
            else:
               return 'Yes'
         elif obj[3] == 'Hold':
            return 'Yes'
         elif obj[3] == 'Buy':
            return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[1] == 'Sell':
      # Feature: SMA1, Instances: 15, Entropy: 0.3534
      if obj[4] == 'Buy':
         return 'Yes'
      elif obj[4] == 'Sell':
         # Feature: Closing, Instances: 7, Entropy: 0.5917
         if obj[0]>37.360001:
            # Feature: SMA2, Instances: 4, Entropy: 0.8113
            if obj[5] == 'Buy':
               # Feature: MACD, Instances: 3, Entropy: 0.9183
               if obj[2] == 'Buy':
                  # Feature: BB, Instances: 3, Entropy: 0.9183
                  if obj[3] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[0]<=37.360001:
            return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[1] == 'Buy':
      return 'No'
   else:
      return 'No'
