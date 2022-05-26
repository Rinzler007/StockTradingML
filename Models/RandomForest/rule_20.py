def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9802
   if obj[3] == 'Sell':
      # Feature: RSI, Instances: 72, Entropy: 0.9978
      if obj[1] == 'Hold':
         # Feature: Closing, Instances: 68, Entropy: 1.0
         if obj[0]<=89.014:
            # Feature: MACD, Instances: 57, Entropy: 0.9944
            if obj[2] == 'Sell':
               # Feature: SMA1, Instances: 34, Entropy: 1.0
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 27, Entropy: 0.9751
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 7, Entropy: 0.5917
                  if obj[5] == 'Buy':
                     return 'Yes'
                  elif obj[5] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[2] == 'Buy':
               # Feature: SMA1, Instances: 23, Entropy: 0.9656
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 20, Entropy: 0.9341
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Buy':
                     return 'Yes'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[0]>89.014:
            # Feature: MACD, Instances: 11, Entropy: 0.8454
            if obj[2] == 'Sell':
               # Feature: SMA2, Instances: 7, Entropy: 0.9852
               if obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 6, Entropy: 1.0
                  if obj[4] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[2] == 'Buy':
               return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[1] == 'Buy':
         return 'No'
      else:
         return 'No'
   elif obj[3] == 'Hold':
      # Feature: Closing, Instances: 40, Entropy: 0.669
      if obj[0]<=89.014:
         # Feature: MACD, Instances: 31, Entropy: 0.7706
         if obj[2] == 'Buy':
            # Feature: RSI, Instances: 24, Entropy: 0.8113
            if obj[1] == 'Hold':
               # Feature: SMA1, Instances: 14, Entropy: 0.8631
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 7, Entropy: 0.8631
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 7, Entropy: 0.8631
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[1] == 'Sell':
               # Feature: SMA1, Instances: 10, Entropy: 0.7219
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 9, Entropy: 0.7642
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[2] == 'Sell':
            # Feature: RSI, Instances: 7, Entropy: 0.5917
            if obj[1] == 'Hold':
               # Feature: SMA1, Instances: 7, Entropy: 0.5917
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 7, Entropy: 0.5917
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[0]>89.014:
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
