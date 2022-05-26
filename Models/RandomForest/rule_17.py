def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9802
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 65, Entropy: 0.9861
      if obj[0]<=75.961998:
         # Feature: RSI, Instances: 56, Entropy: 0.9666
         if obj[1] == 'Hold':
            # Feature: SMA2, Instances: 55, Entropy: 0.971
            if obj[5] == 'Sell':
               # Feature: MACD, Instances: 37, Entropy: 0.9569
               if obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 22, Entropy: 0.976
                  if obj[4] == 'Sell':
                     return 'No'
                  elif obj[4] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 15, Entropy: 0.9183
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               # Feature: MACD, Instances: 18, Entropy: 0.9911
               if obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 16, Entropy: 0.9887
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 2, Entropy: 1.0
                  if obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[1] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[0]>75.961998:
         # Feature: SMA2, Instances: 9, Entropy: 0.9183
         if obj[5] == 'Buy':
            # Feature: SMA1, Instances: 6, Entropy: 0.65
            if obj[4] == 'Buy':
               # Feature: RSI, Instances: 4, Entropy: 0.8113
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 4, Entropy: 0.8113
                  if obj[2] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[4] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[5] == 'Sell':
            # Feature: SMA1, Instances: 3, Entropy: 0.9183
            if obj[4] == 'Sell':
               return 'No'
            elif obj[4] == 'Buy':
               return 'Yes'
            else:
               return 'Yes'
         else:
            return 'No'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: MACD, Instances: 46, Entropy: 0.6666
      if obj[2] == 'Buy':
         # Feature: RSI, Instances: 39, Entropy: 0.7321
         if obj[1] == 'Hold':
            # Feature: SMA1, Instances: 20, Entropy: 0.8813
            if obj[4] == 'Buy':
               # Feature: SMA2, Instances: 13, Entropy: 0.7793
               if obj[5] == 'Buy':
                  # Feature: Closing, Instances: 12, Entropy: 0.65
                  if obj[0]<=75.961998:
                     return 'Yes'
                  elif obj[0]>75.961998:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: SMA2, Instances: 7, Entropy: 0.9852
               if obj[5] == 'Buy':
                  # Feature: Closing, Instances: 4, Entropy: 0.8113
                  if obj[0]<=75.961998:
                     return 'No'
                  elif obj[0]>75.961998:
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[1] == 'Sell':
            # Feature: Closing, Instances: 19, Entropy: 0.4855
            if obj[0]<=75.961998:
               # Feature: SMA1, Instances: 13, Entropy: 0.6194
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 8, Entropy: 0.5436
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 5, Entropy: 0.7219
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[0]>75.961998:
               return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[2] == 'Sell':
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      # Feature: RSI, Instances: 4, Entropy: 0.8113
      if obj[1] == 'Buy':
         # Feature: SMA1, Instances: 2, Entropy: 1.0
         if obj[4] == 'Sell':
            return 'Yes'
         elif obj[4] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[1] == 'Hold':
         return 'No'
      else:
         return 'No'
   else:
      return 'No'
